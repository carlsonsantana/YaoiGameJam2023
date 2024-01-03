transform pan:
    zoom 1.5
    subpixel True
    xalign 0.0
    yalign 0.5
    linear 20.0 xalign 1.0

transform end_pan:
    parallel:
        linear 2.0 zoom 1.0
    parallel:
        linear 2.0 xalign 0.5

transform flip:
    linear 0.2 xzoom -1.0

#transform flip_fade:
#    linear 0.2 alpha 0.0
#    xzoom -1.0 # Flip the image horizontally
#    linear 0.2 alpha 1.0 # Fade in the image in 0.5 seconds

transform jp:
    yoffset 0
    easein 0.25 yoffset -100
    easeout 0.25 yoffset 0
    easein 0.2 yoffset -30
    easeout 0.2 yoffset 0
    easein 0.15 yoffset -10
    easeout 0.15 yoffset 0
    easein 0.1 yoffset -4
    easeout 0.1 yoffset 0
    yoffset 0

transform shake:
    xoffset 0
    easein 0.25 xoffset -100
    easeout 0.25 xoffset 0
    easein 0.2 xoffset -30
    easeout 0.2 xoffset 0
    easein 0.15 xoffset -10
    easeout 0.15 xoffset 0
    easein 0.1 xoffset -4
    easeout 0.1 xoffset 0
    xoffset 0

transform bg_blur:
    linear 2.0 blur 15

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)

transform enter_right:
    yalign 1.0
    xalign 2.0
    linear 0.5 xalign 1.0

transform enter_left:
    yalign 1.0
    xalign -1.0
    linear 0.5 xalign 0.0


define config.side_image_same_transform = same_transform

define left_far = Position(xalign= -2.0, yalign = 1.0)
define center_1left = Position(xalign=0.1, yalign = 1.0)
define center_2left = Position(xalign=0.2, yalign = 1.0)
define center_3left = Position(xalign=0.3, yalign = 1.0)
define center_left = Position(xalign=0.4, yalign = 1.0)

define center_right = Position(xalign=0.6, yalign = 1.0)
define center_2right = Position(xalign=0.8, yalign = 1.0)
define center_3right = Position(xalign=0.85, yalign = 1.0)
define right_far = Position(xalign=2.0, yalign = 1.0)

#define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'overall']
define config.tag_layer['lars'] = 'overlay'

#Audios
define audio.sfx_drum_roll = "sfx_drum_roll.ogg"
define audio.sfx_grassy_walk = "sfx_grassy_walk.ogg"
define audio.sfx_people_talking = "sfx_people_talking.ogg"
define audio.sfx_children_playing = "sfx_children_playing.ogg"
define audio.sfx_clap = "sfx_clap.ogg"
define audio.sfx_smack = "sfx_smack.ogg"
define audio.sfx_splash = "sfx_splash.ogg"

#Otras imagenes
image smoke:
    "images/smoke.png" #with dissolve(0.5, alpha=True)
    alpha 0.00
    easein 1.0 alpha 1.00
    pause 1.0
    easein 1.0 alpha 0.00
    pause 0.5
    repeat

image blink_necklace:
    "images/shining_necklace.png" #with dissolve(0.5, alpha=True)
    alpha 0.00
    easein 0.5 alpha 1.00
    pause 0.1
    easein 0.5 alpha 0.00
    pause 0.1
    repeat

image cg_lars_sylvian_ge:
    "images/cg/cg_lars_sylvian_ge.png"