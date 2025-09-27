import wget
import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Initialize UserAgent once to avoid repeated overhead
_ua = UserAgent()

def get_random_headers(
    referer: str = None,
    accept_language: str = None,
    accept_encoding: str = "gzip, deflate, br",
    connection: str = "keep-alive"
) -> dict:
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

    headers = {
        "User-Agent": _ua.random,
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