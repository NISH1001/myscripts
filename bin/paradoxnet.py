#!/usr/bin/env python3

import sys,os, subprocess
import re
import argparse

risky = ['rm', 'cp', 'mv']

def check_risk(command):
    for r in risky:
        if r in command:
            return False
    return True

def connect_wifi(essid, password):
    command = None
    if not password:
        command = "sudo nmcli dev wifi connect {}".format(essid)
    else:
        command = "sudo nmcli dev wifi connect {0} password {1}".format(essid, password)
    command = command.strip().split()
    if check_risk(command) is False:
        return None

    print("...connecting to {}...".format(essid))

    error = ''
    try:
        output, error = subprocess.Popen(command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE).communicate()
        output = output.decode('utf-8').strip()
        error = error.decode('utf-8').strip()
        if error:
            raise ValueError(error)
        else:
            print("connected to {}".format(essid))
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        print(error)
        sys.exit()

def scan_wifi():
    print("...searching nearby wifi...")
    command = "sudo iwlist wlan0 scan".split()
    if check_risk(command) is False:
        return None
    output, error = subprocess.Popen(command,
            stdout=subprocess.PIPE,
                stderr=subprocess.PIPE).communicate()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    key = re.findall(r'Encryption key:(.*)', output)
    essid = re.findall(r'ESSID:"(.*)"', output)
    return list(zip(essid, key))

def print_essid(l):
    print("nearby connections (ssid) : ")
    print("-"*30)
    for x in l:
        print("{}, password: {}".format(x[0], x[1]))

def main():
    #connect_wifi("YUREKA", "aaaaaaaa")
    #connect_wifi("paradox", "ce2cccb25d8d815d")
    #connect_wifi("a", "aaaaaaaa")
    #print_essid(scan_wifi())

    parser = argparse.ArgumentParser(description="A simple wrapper for network stuffs")

    parser.add_argument("-s","--search", 
            action = 'store_true',
            help="search nearby networks", 
            )
    parser.add_argument("-n", "--name",
            help="nearby network"
            )
    parser.add_argument("-p", "--password",
            help="enter password"
            )

    args = parser.parse_args()

    if args.search:
        print_essid(scan_wifi())

    elif args.name and args.password:
        connect_wifi(args.name, args.password)

    elif args.name:
        connect_wifi(args.name, '')

    else:
        print("LOL! -h or --help for help")

if __name__=="__main__":
    main()

