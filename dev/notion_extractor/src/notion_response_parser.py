from src.notion_api import NotionApi


class NotionResponseParser:
    LOG_ON = True

    def __init__(self):
        self.notion_api = NotionApi()

    def parse_block(self, block_id, indent="", result=""):
        # todo: definitely refactor to be more readable and robust
        block_json = self.notion_api.get_block(block_id)
        for block in block_json["results"]:
            if "paragraph" in block and "rich_text" in block["paragraph"]:
                b = block["paragraph"]
                if "rich_text" in b:
                    c = b["rich_text"]
                    for rich_text in c:
                        if "plain_text" in rich_text:
                            result += f"{indent}{rich_text['plain_text']}"
                    result += "\n"

            if "has_children" in block and block["has_children"]:
                if NotionResponseParser.LOG_ON:
                    print(f"Children found for: {block['id']}")
                result = self.parse_block(block['id'], "    ", result)  # currently 4 spaces
        return result


if __name__ == "__main__":
    parser = NotionResponseParser()
    print(parser.parse_block("dcd4a36bf42a4625a7ac8f7a11cdf846"))
