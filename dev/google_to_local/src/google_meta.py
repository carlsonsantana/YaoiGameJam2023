import json
import os

from src.google_service import GoogleService


class GoogleMeta:
    INDENT = "    "
    CHAR_EXISTS = 1
    CHAR_NOT_EXIST = 0

    LARS_UNKNOWN = 0
    LARS_NORMAL = 1
    LARS_NARRATION = 2

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
        self.lars_mode = GoogleMeta.LARS_UNKNOWN
        self.auto = True
        self.force_hide_lars = False
        self.ignore = False

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
        result = []

        if text_content.strip() == "":
            # ignore empty texts
            return result

        # detect character
        colon_split = text_content.split(":")
        if len(colon_split) < 2:
            print("Skipping...", text_content)
            return result

        # split properly
        char_tag = colon_split[0]
        dialog_tag = ":".join(colon_split[1:]).strip()

        # determine character
        # todo: determine if emotion exists
        # todo: determine if speaker exists and warn user if doesn't
        character = char_tag.split(" ")[0]
        char_details = " ".join(char_tag.split(" ")[1:]).lower()

        if character not in self.character_exists:
            exists = False
            with os.scandir('./game/scripts/characters') as entries:
                for file_entry in entries:
                    # todo look for character
                    curr_path = file_entry.name
                    if curr_path.endswith(".rpy"):
                        exists = curr_path.split(".")[0] == character.lower()
                        if exists:
                            break
            self.character_exists[character] = exists
            if not exists:
                print(f"WARNING: Character does not exist {character}")

        if self.character_exists[character] == GoogleMeta.CHAR_NOT_EXIST:
            character = f"\"{character}\""

        dialog_tag = dialog_tag.replace('"', '\\"')
        dialog_tag = dialog_tag.replace('%', '\%')
        if self.auto:
            if "narration" in char_details:
                if self.lars_mode in [GoogleMeta.LARS_UNKNOWN, GoogleMeta.LARS_NORMAL]:
                    result.append(f"{indent}hide lars\n")
                    self.lars_mode = GoogleMeta.LARS_NARRATION
            else:
                if self.lars_mode in [GoogleMeta.LARS_UNKNOWN, GoogleMeta.LARS_NARRATION]:
                    result.append(f"{indent}show lars at left\n")
                    self.lars_mode = GoogleMeta.LARS_NORMAL

            # todo: bad!
            if self.lars_mode == GoogleMeta.LARS_NARRATION:
                character = "Lars"

        # region possible location of code generation
        # todo: escape double quote?
        # todo: add show character here?
        if self.lars_mode == GoogleMeta.LARS_NARRATION:
            dialog_tag = f"({dialog_tag})"

        result.append(f"{indent}{character} \"{dialog_tag}\"\n\n")
        return result

    @staticmethod
    def transform_to_indented_list(line_list, indent):
        for i in range(len(line_list)):
            line_list[i] = f"{indent}{line_list[i]}\n\n"
        return line_list

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

        # setup
        renpy_lines.extend(GoogleMeta.transform_to_indented_list([
            "call game_setup",
        ], GoogleMeta.INDENT))

        for index, entry in enumerate(google_json):

            if self.ignore:

                lcase = GoogleMeta.extract_element(entry).lower()
                if lcase.startswith("ignore off"):
                    self.ignore = False

                continue

            if index <= skip_index:
                continue

            # todo: support styled text and convert on the spot
            # todo: when a selection is detected, remember the answer
            # todo: addd default at start for option variables
            if "paragraph" in entry:
                paragraph = entry["paragraph"]

                # region detect selection
                if paragraph["paragraphStyle"]["namedStyleType"].startswith("HEADING_2"):
                    # this is a menu!

                    # get selection title
                    selection_title = GoogleMeta.extract_element(entry).split(";")[0]

                    # indent the last line!
                    last_index = len(renpy_lines) - 1
                    renpy_lines[last_index] = GoogleMeta.INDENT + renpy_lines[last_index]

                    # insert a menu tag before the last line
                    renpy_lines.insert(last_index, f"{GoogleMeta.INDENT}menu:\n")
                    target_text = selection_title
                    selection_title = selection_title.replace(" ", "_").strip().lower()

                    # special case
                    special_loop_case = False
                    special_loop_var_list = []
                    if selection_title.startswith("selection_7"):
                        special_loop_case = True

                        # todo: fix hard code
                        renpy_lines.insert(last_index, """    jump selection_7_loop
    return
    
label selection_7_loop:\n""")


                    # todo: find all options until we hit selection ending
                    option_start_index_list = []
                    for option_index in range(index + 1, len(google_json)):
                        option_entry = google_json[option_index]
                        option_text = GoogleMeta.extract_element(option_entry)

                        if option_entry["paragraph"]["paragraphStyle"]["namedStyleType"].startswith("HEADING_3"):
                            option_start_index_list.append(option_index)
                            # print("Options", GoogleMeta.extract_element(google_json[option_index]))

                        if option_text.startswith(target_text):
                            skip_index = option_index
                            break

                    # write down our options


                    renpy_lines.insert(0, f"default {selection_title}_answer = 0\n\n")
                    for index, option_index in enumerate(option_start_index_list):
                        option_entry = google_json[option_index]
                        option_text = GoogleMeta.extract_element(option_entry)

                        if special_loop_case:
                            renpy_lines.append(f"{GoogleMeta.INDENT * 2}\"{option_text.strip()}\" if not selection_7_{index + 1}_done:\n")

                            selection_check = f"{selection_title}_{index + 1}_done"
                            special_loop_var_list.append(selection_check)
                            renpy_lines.insert(0, f"default {selection_check} = False\n\n")
                            renpy_lines.append(f"{GoogleMeta.INDENT * 3}$ {selection_check} = True\n")
                        else:
                            renpy_lines.append(f"{GoogleMeta.INDENT * 2}\"{option_text.strip()}\":\n")


                        renpy_lines.append(f"{GoogleMeta.INDENT * 3}$ {selection_title}_answer = {index + 1}\n")


                        renpy_lines.append(f"{GoogleMeta.INDENT * 3}jump {selection_title}_{index + 1}\n")
                        renpy_lines.append(f"{GoogleMeta.INDENT * 3}return\n\n")

                    # at special_last_index
                    if special_loop_case:
                        renpy_lines.append(f"{GoogleMeta.INDENT}jump google_test_8\n\n")

                    # end the current block
                    partition_count += 1
                    self.lars_mode = GoogleMeta.LARS_UNKNOWN
                    renpy_lines.append(f"{GoogleMeta.INDENT}return\n\n")

                    # write down the dialogs until we a heading (might be a bad idea)
                    # todo: now
                    for index, option_start_index in enumerate(option_start_index_list):
                        renpy_lines.append(f"label {selection_title}_{index + 1}:\n\n")

                        for dialog_index in range(option_start_index + 1, len(google_json)):
                            dialog_entry = google_json[dialog_index]

                            if dialog_entry["paragraph"]["paragraphStyle"]["namedStyleType"].startswith("HEADING_"):
                                # if header, stop!
                                break

                            text_content = self.extract_renpy_line(dialog_entry, GoogleMeta.INDENT)

                            if len(text_content) == 0:
                                continue

                            renpy_lines.extend(text_content)

                        # todo: jump to label instead
                        if special_loop_case:
                            renpy_lines.append(f"{GoogleMeta.INDENT}jump selection_7_loop\n\n")
                        else:
                            renpy_lines.append(f"{GoogleMeta.INDENT}jump {label}_{partition_count}\n\n")

                        self.lars_mode = GoogleMeta.LARS_UNKNOWN
                        renpy_lines.append(f"{GoogleMeta.INDENT}return\n\n")

                    # add the next partition part 2
                    renpy_lines.append(f"label {label}_{partition_count}:\n\n")

                    # todo: create options
                    continue
                # endregion detect selection

                # region detect other heading 6
                if paragraph["paragraphStyle"]["namedStyleType"].startswith("HEADING_6"):
                    # check if if statement
                    lcase = GoogleMeta.extract_element(entry).lower()
                    print("Heading 6 found", lcase)
                    if lcase.startswith("if "):
                        print("IF:", lcase)
                        if_indent = GoogleMeta.INDENT * 2
                        renpy_lines.append(f"{GoogleMeta.INDENT}{lcase}")

                        # run until we find endif
                        for if_index in range(index + 1, len(google_json)):
                            if_entry = google_json[if_index]
                            if_text = GoogleMeta.extract_element(if_entry)

                            if if_entry["paragraph"]["paragraphStyle"]["namedStyleType"].startswith("HEADING_6") \
                                    and if_text.lower().startswith("endif"):
                                skip_index = if_index
                                break

                            text_content = self.extract_renpy_line(if_entry, if_indent)
                            if len(text_content) == 0:
                                continue
                            renpy_lines.extend(text_content)
                    elif lcase.startswith("endif"):
                        pass # ignore
                    elif lcase.startswith("auto on"):
                        self.auto = True
                    elif lcase.startswith("auto off"):
                        self.auto = False
                    elif lcase.startswith("ignore on"):
                        self.ignore = True
                    else:
                        command = lcase.strip()
                        if "bg" in command:
                            # ignore
                            pass
                        elif "show" in command:
                            if "at" in command:
                                command = command.replace("at", "at char_size,")
                            elif "with" in command:
                                command = command.replace("with", "at char_size with")
                            else:
                                command += " at char_size"
                        renpy_lines.append(f"{GoogleMeta.INDENT}{command}\n")

                    continue
                # endregion detect if block

                if paragraph["paragraphStyle"]["namedStyleType"].startswith("HEADING_"):
                    # if header, ignore
                    continue

                text_content = self.extract_renpy_line(entry, GoogleMeta.INDENT)
                if len(text_content) == 0:
                    continue
                renpy_lines.extend(text_content)

        # todo: replace
        with open(dest, "w", encoding="utf-8") as f:
            for line in renpy_lines:
                f.write(line)
