# Love Amidst the Timeless Rift

## How to run dev files

### Setup

1. (Optional) Set up python virtual environment (https://docs.python.org/3/library/venv.html#creating-virtual-environments)
    - Remember to always activate if you're using one! (https://docs.python.org/3/library/venv.html#how-venvs-work)
2. Install python packages with `pip install -r requirements.txt`
3. Create a `.env` file in the root folder. Inside, put the secret key formatted like:
```
NOTION_API_KEY=secret_here_do_not_put_in_git

```
### Scripts ro run from root

#### Notion to local file

```bash
python dev/notion_extractor/notion_extractor.py 
```

#### Local file to renpy

```bash
python dev/renpy_converter/renpy_converter.py 
```

#### Publish web build

```bash
dev/build/build.sh 
```
