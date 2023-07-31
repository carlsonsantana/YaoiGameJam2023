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

### How to use

If you did everything above and there were no issues, just run:

```bash
python dev/google_to_local/complete_google_to_renpy.py
```

This should:

1. Get the latest stuff in our Google Doc
2. Convert that into renpy. The location is at `game/scripts/google_test.py`. Take note that every time you run this
   script, all the changes in `google_test.rpy` will be overwritten, or all the changes made are gonna be removed.

### Typical workflow loop

This is how we want to update our files and see the latest changes.

1. Run `python dev/google_to_local/complete_google_to_renpy.py` to obtain latest Google Doc changes.
2. Run Renpy project or reload using **Shift + R**.
3. Make changes on the **Google Doc** and not on **\*.rpy* since the changes on the latter will be overwritten by step
    1.
4. Repeat step 1 to see changes made during Step 3.

**Rationale: Why do we do this?**

We want one location or one source of truth, not spread out on different files. All our info is in the Google Doc. There
might be some programming stuff in the project repository, but they are independent of the writing in Google Doc. The
other way around also applies.

### Troubleshooting

#### Access blocked: ToRenpy has not completed the Google verification process

![img.png](docs%2Fperm3.png)

@turnip with the email you're using so you could get access to ToRenpy

#### Token expired

I don't have an exact error detail here but you might encounter a 401 error. The solution would be to delete
a `token.json`.

### Scripts to run from root

#### Google Docs to Local file

This is needed to get the Google Docs file back to your computer.

```bash
python dev/google_to_local/google_to_local.py
```

#### Google Local file to renpy

This is the script to run to convert Google Docs to

```bash
python dev/google_to_local/google_to_renpy.py
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

#### Publish web build

For more details, check out [build.md](dev%2Fbuild%2Fbuild.md)

```bash
dev/build/build.sh 
```