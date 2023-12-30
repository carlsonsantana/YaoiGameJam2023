# The script of the game goes in this file.
default persistent.ending = [0,0,0,0,0,0]

define lista_ending = ["Sylvian - Good End", "Sylvian - Neutral End", "Sylvian - Bad End", "Claude - Good End", "Claude - Neutral End", "Claude - Bad End"]
default options = {"C1":0, "C2":0, "CS1":0, "S1":0, "S2":0, "CS2":0, "CS3":0, "CS4":0, "CS5":0, "G1":0, "CS6":0  }
default relations = {"claude":0, "sylvian":0}
default choice_g1 = [0,0]

init python:
    def calc_relations():
        #Reset relations value
        relations["claude"] = 0
        relations["sylvian"] = 0

        if options["C1"]==1:
            relations["claude"]+=1
        elif options["C1"]==2:
            relations["claude"]-=1
        
        if options["C2"]==1:
            relations["claude"]-=1
        elif options["C2"]==2:
            relations["claude"]+=1
        
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

image eileen animated:
    "eileen_happy.png"
    pause 1.0
    "eileen_vhappy.png"
    pause 1.0
    repeat

label splashscreen:
    scene black
    with Pause(1)

    #play sound "ping.ogg"

    show logo with dissolve
    with Pause(2)

    scene bg black with dissolve
    with Pause(1)

    return

# The game starts here.
label start:
    call lattr from _call_lattr

    $ renpy.music.set_volume(0.5)  
    $ renpy.voice.set_mixer("voice")  

    $ renpy.voice.set_character_volume("lars_voice", 1.0)  
    $ renpy.voice.set_character_volume("sylvian_voice", 1.0)  
    $ renpy.voice.set_character_volume("rory_voice", 1.0)  
    $ renpy.voice.set_character_volume("zephyr_voice", 1.0)  
    $ renpy.voice.set_character_volume("claude_voice", 1.0)  

    default persistent._voice_mute = False

    if persistent._voice_mute:
        $ renpy.voice.mute("lars_voice", "sylvian_voice", "rory_voice", "zephyr_voice", "claude_voice")
    else:
        $ renpy.voice.unmute("lars_voice", "sylvian_voice", "rory_voice", "zephyr_voice", "claude_voice")

