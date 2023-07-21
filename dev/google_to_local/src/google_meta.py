import json
import os

from src.google_service import GoogleService


class GoogleMeta:
    INDENT = "    "
    CHAR_EXISTS = 1
    CHAR_NOT_EXIST = 0

    def __init__(self):
        # todo: remove hardcode below or make it optional
        # not really necessary lol
        with open("./dev/google_to_local.json", "r") as f:
            self.meta = json.loads(f.read())

        # todo: add more robust error checking
        self.root = self.meta["root"]
        self.renpy_root = self.meta["renpy_root"]
        self.files = self.meta["files"]

        self.character_exists = {}


    def run_to_local(self):
        service = GoogleService()
        # todo: add more robust error checking
        for file_meta in self.files:
            service.to_local(file_meta["id"], f"{self.root}{file_meta['destination']}")

    def run_to_renpy(self):
        # todo: add more robust error checking
        for file_meta in self.files:
            with open(f"{self.root}{file_meta['destination']}", "r", encoding="utf-8") as f:
                file_content = f.read()
            self.parse_file(file_content, f"{self.renpy_root}{file_meta['renpy']}")  # file closed!


    def parse_file(self, file_content, dest):
        # get the file name and set as label
        label = dest.split("/")[-1]  # get final item
        label = label.split(".")[0]  # get first item

        google_json = json.loads(file_content)
        # todo: more robust error checking
        google_json = google_json["content"]
        num = 0

        with open(dest, "w", encoding="utf-8") as f:
            # todo: add note that this an auto-generated file
            f.write(f"label {label}:\n")

            for entry in google_json:
                # todo: support styled text and convert on the spot
                if "paragraph" in entry:
                    paragraph = entry["paragraph"]
                    if paragraph["paragraphStyle"]["namedStyleType"].startswith("HEADING_"):
                        # if header, ignore
                        continue

                    # put all elements into one text
                    textContent = ""
                    for element in entry["paragraph"]["elements"]:
                        textContent += element["textRun"]["content"]

                    if textContent.strip() == "":
                        # ignore empty texts
                        continue

                    # detect character
                    colon_split = textContent.split(":")
                    if len(colon_split) < 2:
                        print("Skipping...", textContent)
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

                    if self.character_exists[character] == GoogleMeta.CHAR_NOT_EXIST:
                        character = f"\"{character}\""

                    # region possible location of code generation
                    # todo: escape double quote?
                    # todo: add show character here?
                    left_tag = left_tag.replace('"', '\\"')
                    f.write(f"{GoogleMeta.INDENT}{character} \"{left_tag}\"\n\n")
                    # endregion possible location of code generation
                    # print(num, textContent)

                    # num += 1
                    # if num > 10:
                    #     break
                    # if num > 10:
                    #     break
