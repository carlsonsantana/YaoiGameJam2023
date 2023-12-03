# The script of the game goes in this file.
default persistent.ending = [0,0,0,0,0,0]

define lista_ending = ["Sylvian - Good End", "Sylvian - Neutral End", "Sylvian - Bad End", "Claude - Good End", "Claude - Neutral End", "Claude - Bad End"]

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
