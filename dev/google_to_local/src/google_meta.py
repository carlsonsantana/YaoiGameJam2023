import json

from src.google_service import GoogleService


class GoogleMeta:
    def __init__(self):
        # todo: remove hardcode below or make it optional
        # not really necessary lol
        with open("./dev/google_to_local.json", "r") as f:
            self.meta = json.loads(f.read())

        # todo: add more robust error checking
        self.root = self.meta["root"]
        self.files = self.meta["files"]

        self.service = GoogleService()

    def run(self):
        # todo: add more robust error checking
        for file_meta in self.files:
            self.service.to_local(file_meta["id"], f"{self.root}{file_meta['destination']}")
            # self.converter.get_notion_to_local(file_meta["id"], f"{self.root}{file_meta['destination']}")
            pass
