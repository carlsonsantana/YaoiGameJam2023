import os
from os import path

from src.notion_response_parser import NotionResponseParser


class NotionToLocal:
    def __init__(self):
        self.parser = NotionResponseParser()

    def get_notion_to_local(self, block_id, destination):
        to_rpy = self.parser.parse_block(block_id)
        to_rpy = to_rpy.replace("// ", "# ")

        # directory existence check
        directory_split = destination.split("/")
        directory_split.pop()  # remove file
        dir_test = ""
        for dir in directory_split:
            dir_test += dir + "/"
            if dir == ".." or dir == ".":
                pass
            elif not path.exists(dir_test):
                os.mkdir(dir_test)
            elif path.exists(dir_test) and path.isfile(dir_test):
                print(f"Error! Treating file as directory: {dir_test}")

        # save
        with open(destination, "w") as file:
            file.write(to_rpy)
