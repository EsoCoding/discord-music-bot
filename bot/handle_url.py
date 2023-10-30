from urllib.parse import urlparse, parse_qs
from logging import Logger


class HandleUrl:
    def __init__(self):
        pass

    async def validate(self, ctx, arg):
        """
        Validate the given URL and store it in the 'url' attribute of the 'ctx' object.
        try:
            result = urlparse(arg)
            if not all([result.scheme, result.netloc]):
                return ctx.on_command_error("Invalid URL")

        Parameters:
            ctx (object): The context object that stores information about the command.
            arg (str): The URL to be validated.
            if result.netloc not in ["www.qobuz.com", "www.deezer.com"]:
                return ctx.on_command_error("Invalid platform")

        Returns:
            bool: True if the URL is valid and the 'netloc' component is either "www.qobuz.com" or "www.deezer.com". False otherwise.
        """
        try:
            result = urlparse(
                arg
            )  # Parse the given URL and retrieve its components
            ctx.url = arg  # Store the given URL in the 'url' attribute of the 'ctx' object
            Logger.info(
                "Proccesing your gift!"
            )  # Log an informational message
            # Check if both 'scheme' and 'netloc' components of the parsed URL are not empty,
            # and if the 'netloc' component is either "www.qobuz.com" or "www.deezer.com"
            return all([result.scheme, result.netloc]) and (
                result.netloc == "www.qobuz.com"
                or result.netloc == "www.deezer.com"
            )
            ctx.url = arg
            Logger.info("Processing your gift!")
            return True
        except ValueError:
            return ctx.on_command_error("Invalid URL")

    def analyze_url(self, url):
        parsed_url = urlparse(url)
        platform = parsed_url.netloc.split(".")[
            1
        ]  # Extracts 'deezer' or 'qobuz'
        path_parts = parsed_url.path.split("/")

        # Assuming the type (album, track, etc.) is always the second last part of the path
        content_type = path_parts[-2]

        # Assuming the ID is always the last part of the path
        content_id = path_parts[-1]

        platform = parsed_url.netloc.split(".")[1]
        *_, content_type, content_id = parsed_url.path.split("/")

        return platform, content_id
