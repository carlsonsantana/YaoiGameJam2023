import json

from src.notion_api import NotionApi
from src.notion_to_local import NotionToLocal


class NotionMeta:
    def __init__(self):
        self.converter = NotionToLocal()
        self.notion_api = NotionApi()

        # todo: remove hardcode below or make it optional
        # not really necessary lol
        with open("./dev/notion_to_local.json", "r") as f:
            self.meta = json.loads(f.read())

        # todo: add more robust error checking
        self.root = self.meta["root"]
        self.files = self.meta["files"]

    def run(self):
        # todo: add more robust error checking
        for file_meta in self.files:
            self.converter.get_notion_to_local(file_meta["id"], f"{self.root}{file_meta['destination']}")
