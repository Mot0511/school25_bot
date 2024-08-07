import requests

from utils.get_header import get_header


def auth(login: str, password: str) -> str:
    session = requests.Session()
    session.headers.update(get_header())

    url = 'https://passport.43edu.ru/auth/login'
    data = {'login': login, 'password': password, "submit": "submit", "returnTo": "https://one.43edu.ru"}
    session.post(url, data=data, verify=False)

    cookie = next((i for i in session.cookies if i.name == 'X1_SSO'), None)

    return cookie.value, session