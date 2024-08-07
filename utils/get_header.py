from fake_useragent import UserAgent

ua = UserAgent()

def get_header() -> dict:
    return {'User-Agent': str(ua.random)}