# This class represents the MusicBot
from dotenv import load_dotenv
from src.bot import Bot
from logging import Logger

load_dotenv()

logging = Logger()

if __name__ == "__main__":
    bot = Bot()
    bot.start()
