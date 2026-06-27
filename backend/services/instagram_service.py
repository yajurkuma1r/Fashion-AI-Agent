import os

from dotenv import load_dotenv

load_dotenv()


INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")


class InstagramService:
    """
    Handles Instagram Graph API operations.
    """

    def __init__(self):
        self.access_token = INSTAGRAM_ACCESS_TOKEN
        self.account_id = INSTAGRAM_ACCOUNT_ID

    def upload_media(self, image_url: str):
        """
        Creates an Instagram media container.

        Args:
            image_url: Public URL of the generated image.
        """

        raise NotImplementedError

    def publish_media(self, creation_id: str):
        """
        Publishes the uploaded media.

        Args:
            creation_id: Media container ID.
        """

        raise NotImplementedError

    def post_image(self, image_url: str):
        """
        Complete workflow:
        Create media container
        Publish media
        """

        raise NotImplementedError