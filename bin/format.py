#!/usr/bin/env python3

import subprocess
import os
import argparse

class ManualError(Exception):
    def __init__(self, args):
        self.args = args

    def display(self):
        print(''.join(self.args))

def exe(command):
    command = command.strip()
    c = command.split()
    output, error = subprocess.Popen(c,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE).communicate()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    return (output, error)


def format_it(name, sdx='sdc1', form='ext4'):
    name = name.strip()
    user = os.environ.get('USER')
    print("-"*40)
    print(" !CAUTION! do not cancel it in the midway")
    print("-"*40)
    try:
        if "a" in sdx:
            raise ManualError("be sure the partition is sdcx/sdbx :P")

        if not name:
            name = "pendrive"

        name = name.upper()

        print("... unmounting...")
        op, err = exe("sudo umount /dev/{}".format(sdx)) 

        # if already not mounted
        print("... formatting...")
        op, err = exe("sudo mkfs.{} -n '{}' -I /dev/{}".format(form, name, sdx))
        if err:
            print(err)
            raise ManualError("error formatting...")

        path = "/media/pendrive/"
        print("...mounting to {}".format(path))
        op, err = exe("sudo mount -o umask=0 /dev/{} {}".format(sdx, path))
        if err:
            raise ManualError("error mounting after formatting...")

    except KeyboardInterrupt:
        print("keyboard interrupt")
        return False
    except ManualError as merr:
        merr.display()
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="A simple script for formatting the usb")

    parser.add_argument("-sdx", "--sdx",
            help = "which partition"
            )

    parser.add_argument("-n", "--name",
            help = "label name for the partition"
            )

    parser.add_argument("-f", "--form",
            help = "partition type"
            )

    args = parser.parse_args()

    if args.sdx and args.name and args.form:
        format_it(args.name, args.sdx, args.form)
    else:
        print("LOL! just supply freaking parameters... :/")

if __name__=="__main__":
    main()

