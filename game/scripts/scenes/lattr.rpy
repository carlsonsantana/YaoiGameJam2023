define options = {"C1":0, "C2":0, "CS1":0, "S1":0, "S2":0, "CS2":0, "CS3":0, "CS4":0, "CS5":0, "G1":0, "CS6":0  }
define relations = [0, 0, 0]

label lattr:
    $ config.rollback_enabled = False
    scene bg black
    
    python:
        player_name = renpy.input("What is your name?", length=16, default="Lars")
        player_name = player_name.strip()

        if player_name == "":
            player_name = "Lars"

        Lars_name = player_name

    scene bg 1 at bg_size

    $ quick_menu = False

    scene bg black
    #$ cf(3, "opening_scene.mp3")

    pause 1
    scene bg white with dissolve
    scene bg 1 at bg_size with dissolve
    $ quick_menu = True
    $ renpy.block_rollback()
    $ config.rollback_enabled = True

    call part_1 from _call_part_1
    
