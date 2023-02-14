from sqlalchemy import Column, Integer, String, DateTime
from database.db import Base


class User(Base):
    __tablename__ = 'subscribe'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    second_name = Column(String(50))
    nickname = Column(String(50))
    tg_id = Column(Integer, nullable=False)
    phone_number = Column(String(15), nullable=False)
    status = Column(String, nullable=False)

    def __repr__(self):
        return f'Имя {self.first_name} Фамилия {self.second_name} номер телефона {self.phone_number}'
