label lattr:
    $ config.rollback_enabled = False
    scene main_menu 
    show bg black with dissolve
    with Pause(1)
    
    play music "track_1_intro.ogg" fadeout 2.0 fadein 2.0

    python:
        player_name = renpy.input("Please enter your name.", length=16, default="Lars")
        player_name = player_name.strip()

        if player_name == "":
            player_name = "Lars"

        lars_name = player_name

    #scene bg_1 #at bg_size

    $ quick_menu = False

    #scene bg black
    #$ cf(3, "track_0_opening.ogg")

    pause 1
    #scene bg white with dissolve
    #scene bg_1 #at bg_size with dissolve
    $ quick_menu = True
    $ renpy.block_rollback()
    $ config.rollback_enabled = True

    call part_1 from _call_part_1
    
