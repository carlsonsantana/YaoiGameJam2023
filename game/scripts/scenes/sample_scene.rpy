# the colon here is very important!
label sample_scene:
    scene bg room

    show eileen
    eileen "Do you want donut or baguette?"
    
    # the colon here is very important!
    # the game will show the option between donut and baguette like below
    # depending on what the player chooses, the dialog below happens

    menu:
        "Donut please!":
            jump donut

        "Baguette s'il vous plait!":
            jump baguette


label donut:
    eileen "Yay donut!"
    
    # this jump here prevents the dialog in label baguette from appearing after choosing donut
    jump story_continue


label baguette:
    show eileen happy # this shows that the MC will be happy during the next line when MC says "Yay baguette!"

    eileen "Yay baguette!"
    
    jump story_continue


label story_continue:
    "So..."

    return
