import json
import os
import time
import requests
from dotenv import load_dotenv

BLOCK_ID = "dcd4a36bf42a4625a7ac8f7a11cdf846"

load_dotenv()
NOTION_API_KEY = os.getenv("NOTION_API_KEY")


class NotionApi:
    """
    Rate limited API

    Only 3 calls per second!
    """
    CALL_RATE = 1 / 3
    next_call = 0  # global next call time

    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {NOTION_API_KEY}",
        }

    def call_block(self):
        current_time = time.time()

        if current_time < NotionApi.next_call:
            time.sleep(self.next_call - current_time)

        NotionApi.next_call = current_time + NotionApi.CALL_RATE

    def get_block(self, block_id):
        """
        :param block_id: id of a notion block
        :type block_id: string
        :return: parsed json version of the text
        :rtype:
        """
        # todo: error handling
        self.call_block()
        url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
        response = requests.get(url, headers=self.headers)
        return json.loads(response.text)


if __name__ == "__main__":
    # for testing purposes
    api = NotionApi()
    api.get_block(BLOCK_ID)
