#/usr/bin/env bash

echo "Creating noise sample"
ffmpeg -i "$1" -vn -ss 00:00:18 -t 00:00:20 noisesample.wav

echo "Creating noise profile"
sox noisesample.wav -n noiseprof noise_profile

echo "Reducing noise..."
sox "$1" "$2" noisered noise_profile 0.31

echo "Cleaning up..."
rm noisesample.wav
rm noise_profile
