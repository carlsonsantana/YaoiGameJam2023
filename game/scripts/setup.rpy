transform flip:
    linear 0.2 xzoom -1.0

transform unflip:
    linear 0.2 xzoom 1.0

transform flip_instant:
    xzoom -1.0

transform zephyr_intro:
    xalign 0.95
    yalign 0.5

transform zephyr_lower:
    yalign 0.5

transform slight_left:
    xalign 0.2

transform sylvian_at_zephyr_intro:
    xalign 0.65

transform rory_at_zephyr_intro:
    xalign 0.25

transform slight_down:
    yalign 1.15

transform slight_right:
    xalign 0.8

transform more_right:
    xalign 1.2

transform bg_size:
    zoom 0.75

transform market_bg_size:
    zoom 1.5

transform char_size:
    zoom 0.75

transform normal_size:
    zoom 1.0

transform force_normal_size:
    zoom 1.0

transform same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)

define config.side_image_same_transform = same_transform
