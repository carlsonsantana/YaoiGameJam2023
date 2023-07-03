class NotionDirectToRenpy:
    COLON_THRESHOLD = 20
    INDENT = "    "

    def run(self, src: str, dest: str, label: str):
        with open(src, mode="r", encoding="utf-8") as f:
            src_content = f.read()

        with open(dest, mode="w", encoding="utf-8") as f:
            f.write(f"label {label}:\n")
            indent = NotionDirectToRenpy.INDENT

            for line in src_content.split("\n"):
                formatted_line = line.strip()
                # if line starts with # and is ---, ignore
                # ignore empty lines
                if formatted_line in ["", "---"] \
                        or formatted_line.startswith("#"):
                    continue

                # detect narration
                # indents are not pasted out of notion, as a temporary fix,
                # we'll just look for ":" early in the line
                colon_split = formatted_line.split(":")
                left_tag = colon_split[0]
                if len(colon_split) == 1 \
                        or len(left_tag) > NotionDirectToRenpy.COLON_THRESHOLD:
                    # This is a narration so ignore
                    # we might have a different function for this later
                    continue

                # todo: detect character's existence
                character = left_tag.split(" ")[0]
                if self.does_character_exist(character):
                    pass

                # assume that there is a character!
                dialog = ":".join(colon_split[1:]).strip()
                # todo: possible bug when dialog has a quote inside, might need to escape them
                f.write(f"{indent}\"{left_tag}\" \"{dialog}\"\n\n")

    def does_character_exist(self, character):
        character_director = "./game/scripts/characters"


if __name__ == "__main__":
    src = "./dev/notion_test.txt"
    dest = "./game/scripts/notion_test.rpy"

    n = NotionDirectToRenpy()
    n.run(src, dest, "notion_test")
