init python:

    ## For crossfading music
    ## From https://blog.argentgames.co/post/2020-11-16-renpy-crossfade-music/
    renpy.music.register_channel("music1", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    # from: https://fuckyeahrenpy.tumblr.com/post/88995495811/moley-face-i-just-figured-id-post-some-code-i
    def cf(fadeTime, music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel = "music1"
            newChannel = "music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = None
            newChannel = "music"

        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)

        if newChannel is not None:
            renpy.music.play(music, channel=newChannel, loop=None,fadein=fadeTime)