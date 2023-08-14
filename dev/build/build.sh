#!/bin/sh

# for convenience, this assumes that the SDK, this project, and the build directory are all adjacent
# this is run from root! do not run adjacent!
butler push ../love_amidst_the_timeless_rift-1.0-dists/love_amidst_the_timeless_rift-1.0-web.zip deniz-g-lerosi/love-amidst-the-timeless-rift:web

# give everyone else access to the game
#VER_NUM=`cat dev/build/next_version_num.txt`
#GAME_NAME="dev/build/outputs/love_amidst_the_timeless_rift_$VER_NUM"
#echo "$GAME_NAME"
#zip "$GAME_NAME.zip" progressive_download.txt -r game
#butler push "$GAME_NAME.zip" "turnipxenon/love-amidst-the-timeless-rift:renpy_$VER_NUM"
#VER_NUM="$(($VER_NUM + 1))"
#echo "$VER_NUM" >| dev/build/next_version_num.txt
