# This class represents the MusicBot
import os
from dotenv import load_dotenv
from bot.bot import Bot
from logging import Logger
import logging

load_dotenv()

logging = Logger()
logging.basicConfig(level=logging.INFO)


def main():
    bot = Bot()
    bot.start()


if __name__ == "__main__":
    main()
