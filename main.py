# This class represents the MusicBot
import os
from dotenv import load_dotenv
from logging import Logger
from bot.bot import DiscordFastAPIBot



load_dotenv()


if __name__ == "__main__":
    token = os.getenv("DISCORD_BOT_TOKEN")  # Ensure to set this environment variable
    bot = DiscordFastAPIBot(token=os.getenv("DISCORD_BOT_TOKEN"), command_prefix=os.getenv("DISCORD_BOT_PREFIX"))

    bot.run_bot()
