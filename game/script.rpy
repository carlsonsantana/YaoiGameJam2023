# The script of the game goes in this file.

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
