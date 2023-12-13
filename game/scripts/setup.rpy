transform flip:
    linear 0.2 xzoom -1.0

transform unflip:
    linear 0.2 xzoom 1.0

transform flip_instant:
    xzoom -1.0

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
