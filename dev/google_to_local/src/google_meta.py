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

    @staticmethod
    def extract_element(entry):
        if "paragraph" not in entry:
            return ""

        text_content = ""
        for element in entry["paragraph"]["elements"]:
            text_content += element["textRun"]["content"]
        return text_content

    def extract_renpy_line(self, entry, indent):
        # put all elements into one text
        text_content = GoogleMeta.extract_element(entry)

        if text_content.strip() == "":
            # ignore empty texts
            return ""

        # detect character
        colon_split = text_content.split(":")
        if len(colon_split) < 2:
            print("Skipping...", text_content)
            return ""

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
        return f"{indent}{character} \"{left_tag}\"\n\n"

    def parse_file(self, file_content, dest):
        # get the file name and set as label
        label = dest.split("/")[-1]  # get final item
        label = label.split(".")[0]  # get first item

        google_json = json.loads(file_content)
        # todo: more robust error checking
        google_json = google_json["content"]
        partition_count = 1
        renpy_lines = []
        num = 0
        skip_index = -1

        renpy_lines.append(f"label {label}_{partition_count}:\n")
        for index, entry in enumerate(google_json):

            if index <= skip_index:
                continue

            # todo: support styled text and convert on the spot
            if "paragraph" in entry:
                paragraph = entry["paragraph"]

                # region detect selection
                # detect selection
                if paragraph["paragraphStyle"]["namedStyleType"].startswith("HEADING_2"):
                    # this is a menu!

                    # get selection title
                    selection_title = GoogleMeta.extract_element(entry).split(";")[0]

                    # indent the last line!
                    last_index = len(renpy_lines) - 1
                    renpy_lines[last_index] = GoogleMeta.INDENT + renpy_lines[last_index]

                    # insert a menu tag before the last line
                    renpy_lines.insert(last_index, f"{GoogleMeta.INDENT}menu:\n")

                    # todo: find all options until we hit selection ending
                    option_start_index_list = []
                    for option_index in range(index + 1, len(google_json)):
                        option_entry = google_json[option_index]
                        option_text = GoogleMeta.extract_element(option_entry)

                        if option_entry["paragraph"]["paragraphStyle"]["namedStyleType"].startswith("HEADING_3"):
                            option_start_index_list.append(option_index)
                            # print("Options", GoogleMeta.extract_element(google_json[option_index]))

                        if option_text.startswith(selection_title):
                            skip_index = option_index
                            break

                    # write down our options
                    selection_title = selection_title.replace(" ", "_").strip()
                    for index, option_index in enumerate(option_start_index_list):
                        option_entry = google_json[option_index]
                        option_text = GoogleMeta.extract_element(option_entry)
                        renpy_lines.append(f"{GoogleMeta.INDENT*2}\"{option_text.strip()}\":\n")
                        renpy_lines.append(f"{GoogleMeta.INDENT*3}jump {selection_title}_{index}\n\n")

                    # end the current block
                    partition_count += 1
                    renpy_lines.append(f"{GoogleMeta.INDENT}return\n\n")

                    # write down the dialogs until we a heading (might be a bad idea)
                    # todo: now
                    for index, option_start_index in enumerate(option_start_index_list):
                        renpy_lines.append(f"label {selection_title}_{index}:\n\n")

                        for dialog_index in range(option_start_index + 1, len(google_json)):
                            dialog_entry = google_json[dialog_index]

                            if dialog_entry["paragraph"]["paragraphStyle"]["namedStyleType"].startswith("HEADING_"):
                                # if header, stop!
                                break

                            text_content = self.extract_renpy_line(dialog_entry, GoogleMeta.INDENT)

                            if text_content == "":
                                continue

                            renpy_lines.append(text_content)
                        renpy_lines.append(f"{GoogleMeta.INDENT}jump {label}_{partition_count}\n\n")
                        renpy_lines.append(f"{GoogleMeta.INDENT}return\n\n")

                    # add the next partition part 2
                    renpy_lines.append(f"label {label}_{partition_count}:\n\n")

                    # todo: create options
                    continue
                # endregion

                if paragraph["paragraphStyle"]["namedStyleType"].startswith("HEADING_"):
                    # if header, ignore
                    continue

                # put all elements into one text
                text_content = self.extract_renpy_line(entry, GoogleMeta.INDENT)

                if text_content == "":
                    continue

                renpy_lines.append(text_content)

        # todo: replace
        with open(dest, "w", encoding="utf-8") as f:
            for line in renpy_lines:
                f.write(line)
