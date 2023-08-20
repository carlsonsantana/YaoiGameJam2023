transform flip:
    linear 0.2 xzoom -1.0

transform unflip:
    linear 0.2 xzoom 1.0

transform flip_instant:
    xzoom -1.0

transform zephyr_intro:
    xalign 0.95
    yalign 0.5

transform zephyr_lower:
    yalign 0.5

transform slight_left:
    xalign 0.2

transform sylvian_at_zephyr_intro:
    xalign 0.65

transform rory_at_zephyr_intro:
    xalign 0.25

transform slight_down:
    yalign 1.15

transform slight_right:
    xalign 0.8

transform more_right:
    xalign 1.2

transform bg_size:
    zoom 0.75

transform market_bg_size:
    zoom 1.5

transform char_size:
    zoom 0.75

transform normal_size:
    zoom 1.0

transform force_normal_size:
    zoom 1.0

label game_setup:
    scene bg default at bg_size
    return

label name_mc(name_dialog="What is your name?"):
    $ player_name = renpy.input(name_dialog)
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Lars"

    $ Lars = player_name
    return













# old things ignore
label name_mc_v1:
    menu:
        "Name selection process begins."

        "Continue with the standard name \"Lars\"":
            $ player_name = "Lars"
            return

        "Choose my own name":
            menu:
                "It's better to choose the standard name, trust me. Other people call you by your name all throughout the day, so you might as well put yourself in Lars's shoes this time."

                "Continue with the standard name \"Lars\"":
                    $ player_name = "Lars"
                    return


                "Choose my own name":
                    menu:
                        "Either you really like your name, or you're going through an existential crisis and want to escape by having a made-up title. Either way, I should still insist that you change it to Lars. The script makes way more sense that way."

                        "Continue with the standard name \"Lars\"":
                            $ player_name = "Lars"
                            return

                        "Choose my own name":
                            "Fine! Keep your own name if you like it so much. Don't come running back to me if you want to change it again because your it is permanent."

                            menu:
                                "Therefore are you sure?"

                                "Continue with the standard name \"Lars\"":
                                    $ player_name = "Lars"
                                    return

                                "Choose my own name":
                                    $ player_name = "Lars"


    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Lars"

    $ lcase_name = player_name.lower()
    if lcase_name in ["claude", "rory", "sylvian"]:
        "Unknown" "Sorry, that was an invalid name."
        call name_mc from _call_name_mc_1
        return

    menu:
        "Unknown" "Do you want to be called [player_name!q]?"

        "Yes":
            return

        "No":
            call name_mc from _call_name_mc_2