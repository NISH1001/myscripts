#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from collections import OrderedDict

"""
returns a list of list
at index =0, there is header
rest lists are real data
"""
def get_recent(url):
    result = []
    response = requests.get(url)
    if response.status_code != 200:
        return []

    extractor = BeautifulSoup(response.content, "html.parser")
    # content = extractor.find_all("div", {'class': 'block2-content'})[0]
    content = extractor.find_all("div", {'class': 'data_table_wrapper'})[0]
    table = content.find_all(["tr"])

    # table header shit
    table_header = table[0]
    header_list = [ data.get_text() for data in table_header('td') ] [:-1]

    result.append(header_list)

    """
    table = table[1::]
    for row in table:
        table_data = [ td.get_text() for td in row.find_all('td') if not td('form')]
        data = OrderedDict()
        for index, val in enumerate(table_data):
            data[header_list[index]] = val
        result.append(data)
    """

    table = table[1::]
    for row in table:
        table_data = [ td.get_text() for td in row.find_all('td') if not td('form')]
        result.append(table_data)
    return result

def print_table(table):
    table = table[1::]
    for row in table:
        for data in row:
            print("{:15s}".format(data), end='')
        print("\n")

def main():
    url = "http://www.seismonepal.gov.np/"
    print("source: {}".format(url))
    print("-"*100)
    earthquake = get_recent(url)
    print_table(earthquake)

if __name__=="__main__":
    main()

