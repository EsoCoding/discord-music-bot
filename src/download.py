from urllib.parse import urlparse
from logging import Logger
import threading
from src.handle_url import HandleUrl
from src.exceptions import AuthenticationFailed, NotExistingProvider
import streamrip
import os
import asyncio


class Download:
    def __init__(self):
        self.handle_url = HandleUrl()
        self.client_deezer = streamrip.clients.DeezerClient()
        self.client_qobuz = streamrip.clients.QobuzClient()
        self.album = None

    async def download_album(self, ctx, url):
        # 1. validate url and choose
        # which provider to download from
        platform, content_id = self.handle_url.analyze_url(url)

        try:
            if platform == "deezer":
                self.album = streamrip.media.Album(
                    client=self.client_deezer, id=content_id
                )
                self.login(platform)
            elif platform == "qobuz":
                self.album = streamrip.media.Album(
                    client=self.client_qobuz, id=content_id
                )
                # login into qobuz
                self.login(platform)
            else:
                raise NotExistingProvider("Provider not found")

            self.album.load_meta()

            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(None, self.album.download)
            await future

            Logger.info("Download successful")
            return True

        except NotExistingProvider as e:
            raise NotExistingProvider.error(f"Could not select provider {e} ")

    def login(self, platform="qobuz"):
        """Login into qobuz"""

        if platform == "qobuz":
            self.album.client.login(
                email_or_userid=os.environ.get("EMAIL_OR_USERID"),
                use_auth_token=True,
                password_or_token=os.environ.get("PASSWORD_OR_TOKEN"),
            )
        elif platform == "deezer":
            self.album.client.login(arl=os.environ.get("ARL"))

        if self.album.client.logged_in:
            Logger.info("Logged in")
            return True
        else:
            raise AuthenticationFailed("Authentication failed")
