import os
from fastapi import FastAPI
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv
import logging

class DiscordFastAPIBot:
    def __init__(self, token, command_prefix, host="0.0.0.0", port=8000):
        self.token = token
        self.command_prefix = command_prefix
        self.host = host
        self.port = port
        # Initialize FastAPI app
        self.app = FastAPI()

        # Initialize Discord bot
        self.bot = commands.Bot(command_prefix=self.command_prefix, intents=Intents.all())

        self.logging = logging.getLogger(__name__)
        self.logging.setLevel(logging.INFO)
        self.logging.info(f"DiscordFastAPIBot initialized with token: {self.token}")

        # Setup routes and bot events
        self.setup()

    def setup(self):
        @self.app.get("/")
        def read_root():
            return {"Hello": "World"}

        @self.bot.event
        async def on_ready():
            print(f"Logged in as {self.bot.user.name}")

        @self.bot.command(name="hello")
        async def hello(ctx):
            await ctx.send("Hello from Discord bot!")
        
        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')

            # Process commands
            await self.bot.process_commands(message)

    def run_bot(self):
        self.bot.run(self.token)
        
