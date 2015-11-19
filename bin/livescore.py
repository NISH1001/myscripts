#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import sys, argparse

def get_score(url):
    """
    This returns a list of dict.
    The dict of format:
    ['time']    : gives team
    ['team1']   : gives team1 info and is a dict in itself as:
        ['name']
        ['goal']
    ['team2']   : gives team2 info and is a dict in itself as:
        ['name']
        ['goal']
    """
    result = []
    print("...fetching information... from http://www.livescore.com")
    response = requests.get(url)
    if response.status_code != 200:
        return []

    extractor = BeautifulSoup(response.content, "html.parser")
    content = extractor.find_all("div", {'class' : 'row-gray'})
    content2 = extractor.find_all("div", {'class' : 'row-gray even'})
    content += content2

    for match in content:
        text = match.get_text().strip()
        #info = [ x for x in re.split(r"\s+", match.get_text()) if x ]
        info = re.split(r'-', text)

        split1 = info[0].strip()
        split2 = info[1].strip()
        team1_info = split1.split()

        data = {}
        data['time'] = team1_info[0]
        
        team_data = {}
        team_data['goal'] = team1_info[-1]
        team_data['name'] = ' '.join(team1_info[1:-1])

        data['team1'] = team_data

        team_data = {}
        team_data['goal'] = split2[0]
        team_data['name'] = ''.join(split2[1:]).strip()
        
        data['team2'] = team_data

        result.append(data)
    return result

def print_table(scores):
    for score in scores:
        time = score['time']
        team1 = score['team1']
        team2 = score['team2']
        data = [team1['name'], team1['goal'], team2['goal'], team2['name']]
        print(time, "\t", end='')
        for x in data:
            print("{:25s}".format(x), end='')

        print("\n")

def search_team(keyword, data):
    keyword = keyword.lower()
    result = []
    for score in data:
        team1 = score['team1']
        team2 = score['team2']
        if keyword in team1['name'].lower() or  keyword in team2['name'].lower():
            result.append(score)
    return result


"""
def test():
    connection = http.client.HTTPConnection("api.football-data.org")
    headers = { 'X-Auth-Token': 'mytoken', 'X-Response-Control': 'minified' }
    connection.request('GET', '/v1/soccerseasons', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    for x in response:
        print(x)
"""

def main():
    #url = "http://www.livescore.com/soccer/2015-11-19"
    url = "http://www.livescore.com/"

    parser = argparse.ArgumentParser(description="A simple script to get score feed")
    parser.add_argument("-s","--search", 
                        help="search the team/club", 
                    )

    args = parser.parse_args()

    data = get_score(url)
    filtered = None

    if args.search:
        print("search term : ", args.search)
        filtered = search_team(args.search, data)
        print_table(filtered)
    else:
        print_table(data)


if __name__=="__main__":
    main()









