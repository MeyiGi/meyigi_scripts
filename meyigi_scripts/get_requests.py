from bs4 import BeautifulSoup
import requests

def get_requests(url: str, timeout: int = 10, headers: dict = None) -> BeautifulSoup:
    try:
        response = requests.get(url=url, headers=headers)
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