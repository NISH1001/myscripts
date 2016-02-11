#!/usr/bin/env python3

import requests
import json
import urllib.request
import argparse

def get_track_info(url, cid):
    # get track metadata
    api = "http://api.soundcloud.com/resolve.json?url={0}&client_id={1}".format(url, cid)
    response = requests.get(api)
    data = json.loads(response.text)
    return data

def download(stream_url, cid, filename='test'):
    # download the song here
    print(stream_url)
    url = stream_url + "?client_id={0}".format(cid)
    print("... download in progress... :D ")
    try:
        urllib.request.urlretrieve(url, filename+'.mp3')
    except KeyboardInterrupt:
        print(" -_- why y no wait for completion -_-")
        return False
    print("... downloaded 100%, perhaps ... :P")
    return True

def main():
    cid = 'your_client_id_goes_here'

    parser = argparse.ArgumentParser(description="A soundcloud single-track downloader")
    parser.add_argument("-u", "--url",
            help = "soundcloud permalink"
            )

    parser.add_argument("-n", "--name",
            help = "mp3 filename"
            )

    args = parser.parse_args()
    if args.url and args.name:
        track_url = args.url
        filename = args.name
        data = get_track_info(track_url, cid)
        print(data)
        print("-"*40)
        download(data['stream_url'], cid, filename=filename)
    else:
        print("LOL! You are a retard")



if __name__=="__main__":
    main()

