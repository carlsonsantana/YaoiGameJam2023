define Lars = Character("[Lars_name]", color="#C82727", image="lars", voice_tag= "lars")

# image lars = Transform("images/characters/lars.png", xalign=0.0)
image lars hi: 
    "images/characters/lars_default.png"
    xalign 0.0
    zoom 0.75
    alpha 1.0
    linear 0.2 alpha 0.0

image lars: 
    "images/characters/lars_default.png"
    xalign 0.0
    zoom 0.75
    #onlayer overlay

image lars blush: 
    "images/characters/lars_blush.png"
    xalign 0.0
    zoom 0.75

image lars serious:
    "images/characters/lars_serious.png"
    xalign 0.0
    zoom 0.75

image lars happy:
    "images/characters/lars_happy.png"
    xalign 0.0
    zoom 0.75

image lars sad: 
    "images/characters/lars_sad.png"
    xalign 0.0
    zoom 0.75

image lars narration:
    "images/characters/none.png"
    zoom 0.75

image side lars: 
    "images/characters/lars_default.png"
    zoom 0.75

image side lars blush:
    "images/characters/lars_blush.png"
    zoom 0.75

image side lars serious:
    "images/characters/lars_serious.png"
    zoom 0.75

image side lars happy:
    "images/characters/lars_happy.png"
    zoom 0.75

image side lars narration:
    "images/characters/lars narration.png"
    zoom 0.75

image side lars sad: 
    "images/characters/lars_sad.png"
    zoom 0.75

# # Reference: Black Cat 2412 (https://lemmasoft.renai.us/forums/viewtopic.php?p=465239#p465239)
# # Declare characters here
# define config.layers = [ 'master', 'transient','screens','character', 'overlay' ] # make a whole new layer for the character
# define config.tag_layer = {'lars':'character'}  # tag it so every lars image is automatically place on the 'character' layer. Alternatively, you can use "onlayer" to manually put him in there every time
# define config.menu_clear_layers = ['character'] # clear it so the char will disappear when enter game screen, otherwise he will awkwardly stay there

# # We can put character specific subroutines here
#init python:
#    config.side_image_tag = "lars"

#     def custom_command(what, **kwargs):
#         # todo
#         pass

