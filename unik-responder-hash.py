#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Author: 3lDiDi

import argparse
import sys
from os.path import exists


def reader(file, ofile, machine_hash, print_users):
    users = []
    final_hash = []
    nbr_hash = 0

    with open(file, 'r') as data:
        data = data.read().splitlines()
        for hash in data:
            if hash.split():
                user = hash.split('::')[0]
                if user not in users:
                    if len(user) >=2:
                        if machine_hash:
                            users.append(user)
                            final_hash.append(hash)
                        else:
                            if not "$" in user[-1]:
                            users.append(user)
                            final_hash.append(hash)
    
    with open(ofile, 'w') as data:
        for hash in final_hash:
            nbr_hash += 1
            data.write(hash+'\n')
        if print_users:
            print (f"Users :\n{users}")
    print (f"\n[+] {nbr_hash} uniq hashes written to {ofile} !")

    print (f"\nRemember to crack it : hashcat -w 3 -a 0 -m 5600 -O -D 1,2 unik-hash-output.txt <WORDLIST> -r <RULES>")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A program that remove several hashes for a same user. For Responder NetNTLMv2 log file.")
    parser.add_argument("-f","--file", help="File of responder hash to parse.")
    parser.add_argument("-u","--users", default=False, action="store_true", help="Print users parsed from the specified file.")
    parser.add_argument("-m","--machine", default=False, action="store_true", help="Keep the machines NetNTLMv2 hash in the output file. Default these hashes are deleted.")
    parser.add_argument("-o","--output", default="unik-output.txt", help="Output file. Default : unik-output.txt")
    
    args = parser.parse_args()

    if args.file:
        try:
            if exists(args.file):
                reader(args.file, args.output, args.machine, args.users)
            else:
                sys.exit(f"The specified file '{args.file}' was not found.")
        except Exception as error:
            sys.exit(f"ERROR :\nException : {error}")
    else:
        sys.exit("[!] You must specified a NetNTLMv2 file ! Try '-h' for the help.")