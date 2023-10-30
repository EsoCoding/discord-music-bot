import string
import os
import random

from logging import Logger


class Paths:
    def __init__(self):
        self.vowels = "aeiou"
        self.consonants = "".join(
            set(string.ascii_lowercase) - set(self.vowels)
        )

    async def generate(self, ctx, length: int = 10):
        word = ""
        for i in range(length):
            if i % 2 == 0:
                word += random.choice(self.consonants)
            else:
                word += random.choice(self.vowels)

        ctx.client_folder_path = os.path.join(
            os.getenv("DISCORD_BOT_TEMP_FOLDER"), str(word)
        )

        return True

    async def delete(self, ctx):
        try:
            # Log the action of deleting the temp folder along with the unique path
            Logger.info(f"Deleting temp folder: {ctx.client_folder_path}")

            # Use the operating system command "rm -rf" to recursively delete the folder specified by the unique path
            os.system(f"rm -rf {ctx.client_folder_path}")

            # Return True to indicate that the deletion was successful
            return True

        except Exception as e:
            # Log the error message if an exception occurs during the deletion process
            Logger.error(f"Error: {str(e)}")

            # Raise a new exception with the same error message
            raise Exception(f"Error: {str(e)}")
