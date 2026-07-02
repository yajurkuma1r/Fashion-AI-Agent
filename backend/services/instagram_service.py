import os
import requests

from dotenv import load_dotenv

load_dotenv()

INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")


class InstagramService:
    """
    Handles Instagram Graph API operations.
    """

    GRAPH_API_VERSION = "v23.0"

    def __init__(self):
        self.access_token = INSTAGRAM_ACCESS_TOKEN
        self.account_id = INSTAGRAM_ACCOUNT_ID

    def upload_media(self, image_url: str) -> str:
        """
        Creates a media container.

        Returns:
            Creation ID.
        """

        endpoint = (
            f"https://graph.facebook.com/"
            f"{self.GRAPH_API_VERSION}/"
            f"{self.account_id}/media"
        )

        payload = {
            "image_url": image_url,
            "access_token": self.access_token,
        }

        response = requests.post(endpoint, data=payload)
        response.raise_for_status()

        return response.json()["id"]

    def publish_media(self, creation_id: str):
        """
        Publishes a media container.
        """

        endpoint = (
            f"https://graph.facebook.com/"
            f"{self.GRAPH_API_VERSION}/"
            f"{self.account_id}/media_publish"
        )

        payload = {
            "creation_id": creation_id,
            "access_token": self.access_token,
        }

        response = requests.post(endpoint, data=payload)
        response.raise_for_status()

        return response.json()

    def post_image(self, image_url: str):
        """
        Complete workflow.

        Upload image
            ↓
        Publish image
        """

        creation_id = self.upload_media(image_url)

        return self.publish_media(creation_id)