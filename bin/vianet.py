#!/usr/bin/env python3

import requests, json, os
from bs4 import BeautifulSoup
from collections import OrderedDict

class ManualError(Exception):
    def __init__(self, args):
        self.args = args

    def display(self):
        print(''.join(self.args))

def load_payload(filename="data/vianet.json"):
    config = {}
    try:
        configstr = open(filename).read()
        config = json.loads(configstr)
    except ManualError as merr:
        merr.display()
    return config

def scrap(url):
    result = OrderedDict()

    path = os.path.dirname(os.path.abspath(__file__))
    payload = load_payload(path + "/data/vianet.json")
    session = requests.session()

    print("...fetching information from vianet...")
    response = session.post(url, data = payload)

    try:
        if response.status_code != 200:
            raise ManualError("error fetching...")
        else:
            response = session.get(payload["url"])
            extractor = BeautifulSoup(response.content, "html.parser")
            table = extractor.select('tr')

            for row in table:
                tr = row.find_all('td')
                if tr:
                    result[tr[0].get_text()] = tr[1].get_text()
    except KeyboardInterrupt:
        print("quit...")
    except ManualError as merr:
        merr.display()

    return result

def display(data):
    print()
    print("-"*80)
    print("vianet services")
    print("-"*80)

    for key in data:
        print("{:25s} : {:10s}".format(key, data[key]))


def main():
    url = "https://customers.vianet.com.np/portal/login.pl"
    data = scrap(url)
    if data:
        display(data)

if __name__=="__main__":
    main()

