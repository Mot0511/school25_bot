from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    id: Mapped[int] = Column(Integer, unique=True, autoincrement=True, primary_key=True)

class User(Base):
    __tablename__ = 'users'

    uid: int = Column(Integer, unique=True)
    login: str = Column(String, unique=True)
    hashed_password: str = Column(String)