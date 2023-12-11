transform flip:
    linear 0.2 xzoom -1.0

transform unflip:
    linear 0.2 xzoom 1.0

transform flip_instant:
    xzoom -1.0

#transform zephyr_intro:
#    xalign 0.95
#    yalign 0.5

#transform zephyr_lower:
#    yalign 0.5

#transform slight_left:
#    xalign 0.2

#transform sylvian_at_zephyr_intro:
#    xalign 0.65

#transform rory_at_zephyr_intro:
#    xalign 0.25

#transform slight_down:
#    yalign 1.15

#transform slight_right:
#    xalign 0.8

#transform more_right:
#    xalign 1.2

#transform bg_size:
#    zoom 0.75

#transform market_bg_size:
#    zoom 1.5

#transform char_size:
#    zoom 0.75

#transform normal_size:
#    zoom 1.0

#transform force_normal_size:
#    zoom 1.0
transform bg_blur:
    linear .25 blur 15

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)


define config.side_image_same_transform = same_transform

define center_left = Position(aling=0.4)

define center_right = Position(aling=0.6)

#define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'overall']
define config.tag_layer['lars'] = 'overlay'

#Audios
define audio.sfx_drum_roll = "sfx_drum_roll.mp3"
define audio.sfx_grassy_walk = "sfx_grassy_walk.mp3"
define audio.sfx_people_talking = "sfx_people_talking.mp3"
define audio.sfx_children_playing = "sfx_children_playing.mp3"
define audio.sfx_clap = "sfx_clap.mp3"
define audio.sfx_smack = "sfx_smack.mp3"
define audio.sfx_splash = "sfx_splash.mp3"

#Otras imagenes
image smoke:
    "images/smoke.png" #with dissolve(0.5, alpha=True)
    alpha 0.00
    easein 1.0 alpha 1.00
    pause 1.0
    easein 1.0 alpha 0.00
    pause 0.5
    repeat
