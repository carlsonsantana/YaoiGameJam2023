"""
NotionExtractor aims to extract the files from Notion and places them as text files
for easier parsing
"""


from src.notion_meta import NotionMeta

DIRECTORY_ID = "080c687dbef748e48bf9582f4d9a6af4"

if __name__ == "__main__":
    # get all children
    # iterate through everyone
    # save them to the correct location
    handler = NotionMeta()
    handler.run()
