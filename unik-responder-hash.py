#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Author: 3lDiDi

import argparse
import sys
from os.path import exists

def reader(file, ofile="unik-output.txt"):
    users = []
    final_hash = []
    nbr_hash = 0
    with open(file, 'r') as data:
        data = data.read().splitlines()
        for hash in data:
            user = hash.split('::')[0]
            if user not in users:
                users.append(user)
                final_hash.append(hash)
    
    with open(ofile, 'w') as data:
        for hash in final_hash:
            nbr_hash += 1
            data.write(hash+'\n')
    print (f"{nbr_hash} uniq hashes written to {ofile} !")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A program that remove several hash for a same user. It is a Responder log parser.")
    parser.add_argument("-f","--file", help="File of responder hash to parse.")
    parser.add_argument("-o","--output", help="Output file.")
 
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()

    if args.file:
        reader(args.file, args.output)
