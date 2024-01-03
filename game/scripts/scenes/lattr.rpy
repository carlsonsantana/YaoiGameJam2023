label lattr:
    $ config.rollback_enabled = False
    scene main_menu 
    show bg black with dissolve
    with Pause(1)
    
    play music "track_1_intro.ogg" fadeout 2.0 fadein 2.0

    python:
        player_name = renpy.input("Could you kindly tell us your name? If you don’t have a preference, we’d be delighted to use ‘Lars’ as the default.)", length=16, default="Lars")
        player_name = player_name.strip()

        if player_name == "":
            player_name = "Lars"

        Lars_name = player_name

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
    
