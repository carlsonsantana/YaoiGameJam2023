# Love Amidst the Timeless Rift

## How to run dev files

### Setup

1. Install python packages with `pip install -r requirements.txt`
2. If you haven't make sure you're logged into the account with access to the Google Doc.
3. Run `python dev/google_to_local/complete_google_to_renpy.py`
4. A browser should pop up and you choose that email
5. Press Continue on the left and not Back to safety
   - ![perm1.png](docs%2Fperm1.png)
6. Select all and then Continue
    - ![perm2.png](docs%2Fperm2.png)

### Scripts to run from root

### Google Docs to Local file

This is needed to get the Google Docs file back to your computer.

```bash
python dev/google_to_local/google_to_local.py
```

### Google Local file to renpy

This is the script to run to convert Google Docs to

```bash
python dev/google_to_local/google_to_renpy.py
```

#### Publish web build

```bash
dev/build/build.sh 
```

## Remote to local to renpy

This gets the Google Doc and converts it to renpy. The entire process.

**Option 1**
```bash
python dev/google_to_local/complete_google_to_renpy.py
```

**Option 2**
```bash
python dev/google_to_local/google_to_local.py && python dev/google_to_local/google_to_renpy.py
```
