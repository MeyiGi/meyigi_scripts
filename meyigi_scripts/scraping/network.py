import random
import requests
import httpx
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from typing import Optional, Dict

# Initialize UserAgent once to avoid repeated overhead
_ua = UserAgent()

async def get_async_requests(url: str, timeout: int = 10, headers: dict = None) -> BeautifulSoup:
    """Asynchronously makes a GET request and returns a BeautifulSoup object.

    Args:
        url (str): The target URL for the GET request.
        timeout (int, optional): Timeout in seconds. Defaults to 10.
        headers (dict, optional): Optional headers for the request. Defaults to None.

    Raises:
        httpx.HTTPStatusError: If the request returns a 4xx or 5xx status code.
        httpx.TimeoutException: If the request times out.
        httpx.RequestError: For other network-related errors.

    Returns:
        BeautifulSoup: A BeautifulSoup object of the page content.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "lxml")
        return soup

    except httpx.HTTPStatusError as e:
        raise httpx.HTTPStatusError(f"HTTP Error: {e.response.status_code} for url: {e.request.url}", request=e.request, response=e.response)
    except httpx.TimeoutException as e:
        raise httpx.TimeoutException("The request timed out.", request=e.request)
    except httpx.RequestError as e:
        raise httpx.RequestError(f"A network error occurred: {e}", request=e.request)
    
def get_random_headers(
    referer: Optional[str] = None,
    accept_language: Optional[str] = None,
    accept_encoding: str = "gzip, deflate, br",
    connection: str = "keep-alive"
) -> Dict[str, str]:
    """
    Generate random HTTP headers for making web requests.

    :param referer: Optional Referer header value. If None, it will be excluded.
    :param accept_language: Optional Accept-Language header value. If None, a random language is chosen.
    :param accept_encoding: Accept-Encoding header value. Defaults to common encodings.
    :param connection: Connection header value. Defaults to "keep-alive".
    :return: A dictionary of HTTP headers.
    """
    if accept_language is None:
        # Randomize language preference
        languages = [
            "en-US,en;q=0.9",
            "en-GB,en;q=0.8",
            "fr-FR,fr;q=0.9,en;q=0.8",
            "de-DE,de;q=0.9,en;q=0.8",
            "es-ES,es;q=0.9,en;q=0.8"
        ]
        accept_language = random.choice(languages)

    # NOTE: this project expects a Desktop Chrome User-Agent here.
    # The internal browser._get_desktop_user_agent() explicitly filters for
    # desktop-like UAs — keep the behavior here consistent with that function.
    # _ua.random is expected to provide a Desktop Chrome UA in this codebase.
    user_agent: str = _ua.random

    headers: Dict[str, str] = {
        "User-Agent": user_agent,
        "Accept-Language": accept_language,
        "Accept-Encoding": accept_encoding,
        "Connection": connection,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1"
    }

    if referer:
        headers["Referer"] = referer

    return headers

def get_requests(url: str, timeout: int = 10, headers: dict = None) -> BeautifulSoup:
    """Simplifications of getting requests

    Args:
        url (str): Url of content to get content
        timeout (int, optional): Time to wait until getting content. Defaults to 10.
        headers (dict, optional): headers to attach for requests. Defaults to None.

    Raises:
        requests.exceptions.HTTPError
        requests.exceptions.ReadTimeout
        requests.exceptions.ConnectionError
        requests.exceptions.RequestException

    Returns:
        BeautifulSoup: content of page to interact with BS4

    Examples:
        soup: BeautifulSoup = get_requests("www.youtube.com")
        print(soup.prettify())
    """
    try:
        response = requests.get(url=url, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        raise requests.exceptions.HTTPError("HTTP Error: {errh}")
    except requests.exceptions.ReadTimeout as errR:
        raise requests.exceptions.ReadTimeout("Time out exceeded, please specify more time for requests")
    except requests.exceptions.ConnectionError as errC:
        raise requests.exceptions.ConnectionError("Connection error: {errC.args}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f'RequestsException: {str(e)}')
        
    soup = BeautifulSoup(response.text, "lxml")

    return soup