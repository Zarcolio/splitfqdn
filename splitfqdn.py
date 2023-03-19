#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import signal
import argparse
import re

from tldextract import extract

def signal_handler(sig, frame):
    sys.stderr.write("\nCtrl-C detected, quitting...\n")
    sys.exit(0)

def main(args):
    try:
        for sInFqdn in sys.stdin:
            sInFqdn = sInFqdn.strip()
            if not sInFqdn:
                continue

            # Extract domain levels using tldextract
            dl3, dl2, dl1 = extract(sInFqdn)

            # Replace format string with domain levels
            sOutput = args.format.replace("%1", dl1).replace("%2", dl2).replace("%3", dl3)

            # Replace remaining domain levels using split
            if not args.extract321:
                aFqdnSplit = sInFqdn.rsplit(dl1, 1)[0].split(".")
                for i, sDomainLevel in enumerate(aFqdnSplit[::-1], start=1):
                    if i > 9:
                        break
                    sOutput = sOutput.replace(f"%{i}", sDomainLevel)

            # Print output
            if not args.fullmatch or not re.match(r".*%[0-9]", sOutput):
                print(sOutput)

    except UnicodeError:
        pass

signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser()
parser.add_argument("format", help="%%1 to %%9 is replaced with the corresponding domain level taken from the input (takes vTLD such as co.uk into account). For example, if the argument %%3.%%2.%%1 is given and stdin supplies sub5.sub4.sub3.example.co.uk then sub3.example.co.uk is returned. The dots are free-form, any character can be used.")
parser.add_argument("-321", "--extract321", help="Separeate second (%%2) and top level domain (%%1), and the remaining part (%%3).", action="store_true")
parser.add_argument("-full", "--fullmatch", help="Only show those lines that have all %%1-%%9 have replaced.", action="store_true")
args = parser.parse_args()

if __name__ == '__main__':
    main(args)
