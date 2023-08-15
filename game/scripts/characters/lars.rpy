define Lars = Character("Lars", image="lars")

image side lars = "lars.png"
image side lars blush = "lars blush.png"
image side lars happy = "lars happy.png"
image side lars serious = "lars serious.png"

# Reference: Black Cat 2412 (https://lemmasoft.renai.us/forums/viewtopic.php?p=465239#p465239)
# Declare characters here
define config.layers = [ 'master', 'transient','screens','character', 'overlay' ] # make a whole new layer for the character
define config.tag_layer = {'lars':'character'}  # tag it so every lars image is automatically place on the 'character' layer. Alternatively, you can use "onlayer" to manually put him in there every time
define config.menu_clear_layers = ['character'] # clear it so the char will disappear when enter game screen, otherwise he will awkwardly stay there

# We can put character specific subroutines here
init python:
    config.side_image_tag = "lars"

    def custom_command(what, **kwargs):
        # todo
        pass
