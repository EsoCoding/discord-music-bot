from io import BytesIO
from logging import Logger
import aiohttp

class Uploader:
    def __init__(self):
        self.buffer = BytesIO()

    async def get_gofile_server(self):
        gofile_alive_url = "https://api.gofile.io/getServer"
        async with aiohttp.ClientSession() as session:
            async with session.get(gofile_alive_url) as response:
                data = await response.json()
                if data["status"] == "ok":
                    Logger.info("Connection with gofile.io established")
                    return data['data']['server']
                else:
                    Logger.error("Connection with gofile.io failed")
                    raise ConnectionError("Connection with gofile.io failed")

    async def upload_file_to_gofile(self, server, file_path):
        upload_url = f"https://{server}.gofile.io/uploadFile"
        Logger.info(f"Uploading file to url: {upload_url}")
        async with aiohttp.ClientSession() as session:
            with open(file_path, "rb") as file:
                form = aiohttp.FormData()
                form.add_field("file", file)
                async with session.post(upload_url, data=form) as response:
                    return await response.json()

    def handle_upload_response(self, response):
        if response["status"] == "ok":
            Logger.info("Upload successful")
            return str(response["data"]["downloadPage"])
        else:
            Logger.error(f"Upload failed, response code: {response['status']}")
            raise ValueError(f"Upload failed, response code: {response['status']}")

    async def upload_file(self, ctx) -> None:
        try:
            Logger.info("Trying to upload file to gofile.io")
            server = await self.get_gofile_server()
            response = await self.upload_file_to_gofile(server, str(ctx.album_path) + "/"+ str(ctx.album_name)+".zip")
            ctx.go_file_link = self.handle_upload_response(response)
            return True
        except Exception as e:
            Logger.error(f"Error: {str(e)}")
            raise ValueError(f"Upload failed, error {str(e)}")