from database.model import *
from database.db import Base, engine
from bot.bot import tg_bot

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    tg_bot()   
