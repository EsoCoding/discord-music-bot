import os
from fastapi import FastAPI
from discord.ext import commands
from discord import Intents
import uvicorn 
from dotenv import load_dotenv


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

        # Setup routes and bot events
        self.setup()

    def setup(self):
        @self.app.get("/")
        def read_root():
            return {"Hello": "World"}

        @self.bot.event
        async def on_ready():
            print(f"Logged in as {self.bot.user}")

        @self.bot.command(name="download")
        async def download(ctx):
            await ctx.send("Hello from Discord bot!")

    def run(self):
        # Run the FastAPI server
        load_dotenv()

        uvicorn.run(self.app, host=self.host, port=self.port)
        # Run the Discord bot
        self.bot.run(self.token)

