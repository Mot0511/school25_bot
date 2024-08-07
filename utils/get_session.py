from requests import Session
import requests
from sqlalchemy import select
from db.engine import sessionmaker
from utils.get_header import get_header


async def get_session(token: str) -> Session:

    cookies = {'X1_SSO': token}

    session = requests.Session()
    session.headers.update(get_header())
    session.cookies.update(cookies)
    session.get("https://one.43edu.ru/")

    return session