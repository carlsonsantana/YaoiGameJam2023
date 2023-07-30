# Build

This documentation is for building the game into a playable application.

## Current workflow

### Requirements

- [Butler](https://itch.io/docs/butler/installing.html)
  - Follow the install process for your OS
  - Log in! You'll need to have an itch.io account
  - Make sure your account has access to the game project. @turnip to get access
- You must have the renpy builds adjacent to this project! For example:
```
- random_folder
    - love_amidst_the_timeless_rift-1.0-dists (the builds)
        - love_amidst_the_timeless_rift-1.0-web
        - love_amidst_the_timeless_rift-1.0-web.zip
    - YaoiGameJam2023 (the project)
        - games
        - README.md
        - (you are currently here!!!)
    - renpy-8.1.1-sdk (your renpy SDK or exe here but it can work even if it's not here)
        - renpy.exe
```

### Process

For web builds, the current workflow follows:

1. Open the **Ren'py Launcher**. Go to **Web (Beta)**, and **Build Web Application**.
2. Run `butler push love_amidst_the_timeless_rift-1.0-web.zip turnipxenon/love-amidst-the-timeless-rift` whereever the
    zip build is located.

### Rationale

We can distribute Linux and Windows automatically, but we can't distribute Web automatically. Although,
web distribution is the easiest for everyone to see iteration faster, so I'm sticking to that.

In the future, I'll investigate further how to support that, and make iteration faster.
