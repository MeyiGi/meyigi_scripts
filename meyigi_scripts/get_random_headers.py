from fake_useragent import UserAgent

def get_random_headers(
    referer: str = None,
    accept_language: str = "en-US,en;q=0.9",
    accept_encoding: str = "gzip, deflate, br",
    connection: str = "keep-alive"
) -> dict:
    """
    Generate random HTTP headers for making web requests.

    :param referer: Optional Referer header value. If None, it will be excluded.
    :param accept_language: Accept-Language header value. Defaults to English.
    :param accept_encoding: Accept-Encoding header value. Defaults to common encodings.
    :param connection: Connection header value. Defaults to "keep-alive".
    :return: A dictionary of HTTP headers.
    """
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": accept_language,
        "Accept-Encoding": accept_encoding,
        "Connection": connection
    }

    if referer:
        headers["Referer"] = referer

    return headers