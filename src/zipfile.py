# this class handles the zip 
# process of the downloaded mp3 files.
# the temp folder which is 
# used to store the downloaded 
# is the ctx.album_path where the files are
# and the name of that new folder is ctx.album name
# When finished zipping, check if zipfile really exist
# and if the its at least a small size to be sure its not empty

import os
import zipfile
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ZipFile:
    def __init__(self):
        self.executor = ThreadPoolExecutor()

    async def zip(self, ctx):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, self._zip, ctx)

    def zipfile(self, ctx):
        try:
            with zipfile.ZipFile(f"{ctx.album_path}/{ctx.album_name}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(ctx.album_path):
                    for file in files:
                        full_file_path = os.path.join(root, file)
                        relative_file_path = os.path.relpath(full_file_path, ctx.album_path)
                        zipf.write(full_file_path, relative_file_path)

            if os.path.exists(f"{ctx.album_path}/{ctx.album_name}.zip"):
                ctx.go_file_link = f"{ctx.album_path}/{ctx.album_name}.zip"
                return True
            else:
                raise Exception("Zip failed")
        except Exception as e:
            raise Exception(f"An error occurred while zipping: {str(e)}")
