define options = {"C1":0, "C2":0, "CS1":0, "S1":0, "S2":0, "CS2":0, "CS3":0, "CS4":0, "CS5":0, "G1":0, "CS6":0  }
define relations = {"claude":0, "sylvian":0}

init python:
    def calc_relations():
        #Reset relations value
        relations["claude"] = 0
        relations["sylvian"] = 0

        if options["C1"]==1:
            relations["claude"]-=1
        elif options["C1"]==2:
            relations["claude"]+=1
        
        if options["C2"]==1:
            relations["claude"]+=1
        elif options["C2"]==2:
            relations["claude"]-=1
        
        if options["CS1"]==1:
            relations["claude"]+=1
        elif options["CS1"]==2:
            relations["sylvian"]+=1
        
        if options["S1"]==1:
            relations["sylvian"]+=1
        elif options["S1"]==2:
            relations["sylvian"]-=1
        
        if options["S2"]==1:
            relations["sylvian"]+=1
        elif options["S2"]==2:
            relations["sylvian"]-=1
        
        if options["CS2"]==1:
            relations["sylvian"]+=1
        elif options["CS2"]==2:
            relations["claude"]+=1
        
        if options["CS3"]==1:
            relations["sylvian"]+=1
        elif options["CS3"]==2:
            relations["claude"]+=1
        
        if options["CS4"]==1:
            relations["sylvian"]+=1
        elif options["CS4"]==2:
            relations["claude"]+=1
        
        if options["CS5"]==1:
            relations["sylvian"]+=1
        elif options["CS5"]==2:
            relations["claude"]+=1
        
        if options["CS6"]==1:
            relations["sylvian"]+=1
        elif options["CS6"]==2:
            relations["claude"]+=1


label lattr:
    $ config.rollback_enabled = False
    scene bg black
    
    python:
        player_name = renpy.input("What is your name?", length=16, default="Lars")
        player_name = player_name.strip()

        if player_name == "":
            player_name = "Lars"

        Lars_name = player_name

    #scene bg_1 #at bg_size

    $ quick_menu = False

    #scene bg black
    $ cf(3, "opening_scene.mp3")

    pause 1
    #scene bg white with dissolve
    #scene bg_1 #at bg_size with dissolve
    $ quick_menu = True
    $ renpy.block_rollback()
    $ config.rollback_enabled = True

    call part_1 from _call_part_1
    
