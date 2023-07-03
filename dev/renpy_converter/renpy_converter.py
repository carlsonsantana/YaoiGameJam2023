import json
import os


class RenpyConverter:
    INDENT = "    "
    CHAR_EXISTS = 1
    CHAR_NOT_EXIST = 0

    def __init__(self):
        with open("./dev/notion_to_local.json", "r") as f:
            self.meta = json.loads(f.read())

        # todo: add more robust error checking
        self.root = self.meta["root"]
        self.renpy_root = self.meta["renpy_root"]
        self.files = self.meta["files"]

        self.character_exists = {}

    def run(self):
        # todo: obtain all files
        for file_meta in self.files:
            with open(f"{self.root}{file_meta['destination']}", "r", encoding="utf-8") as f:
                file_content = f.read()
            self.parse_file(file_content, f"{self.renpy_root}{file_meta['renpy']}")  # file closed!

    def parse_file(self, file_content, dest):
        # get the file name and set as label
        label = dest.split("/")[-1]  # get final item
        label = label.split(".")[0]  # get first item

        with open(dest, "w", encoding="utf-8") as f:
            f.write(f"label {label}:\n")

            for line in file_content.split("\n"):
                # ignore empty lines
                if line == "":
                    continue

                # ignore lines indented with four spaces
                if line.startswith(RenpyConverter.INDENT):
                    continue

                colon_split = line.split(":")
                if len(colon_split) < 2:
                    print("Skipping...", line)
                    continue

                # split properly
                right_tag = colon_split[0]
                left_tag = ":".join(colon_split[1:]).strip()

                # determine character
                # todo: determine if emotion exists
                # todo: determine if speaker exists and warn user if doesn't
                character = right_tag.split(" ")[0]

                if character not in self.character_exists:
                    exists = False
                    with os.scandir('./game/scripts/characters') as entries:
                        for entry in entries:
                            # todo look for character
                            curr_path = entry.name
                            if curr_path.endswith(".rpy"):
                                exists = curr_path.split(".")[0] == character.lower()
                                if exists:
                                    break
                    self.character_exists[character] = exists
                    if not exists:
                        print(f"WARNING: Character does not exist {character}")

                if self.character_exists[character] == RenpyConverter.CHAR_NOT_EXIST:
                    character = f"\"{character}\""

                # todo: escape double quote
                f.write(f"{RenpyConverter.INDENT}{character} \"{left_tag}\"\n\n")


if __name__ == "__main__":
    # get all children
    # iterate through everyone
    # save them to the correct location
    handler = RenpyConverter()
    handler.run()
