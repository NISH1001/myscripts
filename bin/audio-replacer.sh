#/usr/bin/env bash

# replace audio in a video by another audio
# $1 -> input video
# $2 -> input audio
# $3 -> output video
ffmpeg -i "$1" -i "$2" -c:v copy -map 0:v:0 -map 1:a:0 "$3"

