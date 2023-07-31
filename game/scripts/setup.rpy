transform bg_size:
    zoom 0.75

transform char_size:
    zoom 0.75

label game_setup:
    call name_mc
    $ Lars = player_name
    scene bg default at bg_size
    return

label name_mc:
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Lars"

    $ lcase_name = player_name.lower()
    if lcase_name in ["claude", "rory", "sylvian"]:
        "Unknown" "Sorry, that was an invalid name."
        call name_mc
        return

    menu:
        "Unknown" "Do you want to be called [player_name!q]?"

        "Yes":
            return

        "No":
            call name_mc