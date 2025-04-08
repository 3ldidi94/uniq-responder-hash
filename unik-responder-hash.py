#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Author: 3lDiDi

import argparse
import sys
from os.path import exists

GREEN="\033[92m"
YELLOW="\033[33m"
RED="\033[91m"
BLUE="\033[94m"
Default="\033[0m"

def reader(file, ofile, machine_hash, print_users, users_only):
    users = []
    final_hash = []
    nbr_hash = 0

    with open(file, 'r') as data:
        data = data.read().splitlines()
        for hash in data:
            user = hash.split('::')[0]
            if user not in users:
                if machine_hash:
                    users.append(user)
                    final_hash.append(hash)
                else:
                    if not "$" in user[-1]:
                        users.append(user)
                        final_hash.append(hash)
    
    nbr_hash = len(final_hash)

    if not users_only:
        with open(ofile, 'w') as data:
            for hash in final_hash:
                #nbr_hash += 1
                data.write(hash+'\n')
            if print_users:
                print (f"{YELLOW}Captured users:\n")
                for user in users:
                    print (f"{GREEN}{user}{Default}")
                ## Print users in list format
                #print (f"Users :\n{users}")

        print (f"\n{YELLOW}[+] {nbr_hash} uniq hashes written to{Default} {ofile} {YELLOW}!{Default}")
    
    elif users_only:
        for user in users:
            print (f"{GREEN}{user}{Default}")
        print (f"\n{YELLOW}[+] {GREEN}{nbr_hash} {YELLOW}uniq hashes parsed !{Default}")

    print (f"\n{RED}Remember, to crack it:{Default} hashcat -w 3 -a 0 -m 5600 -O -D 1,2 unik-hash-output.txt <WORDLIST> -r <RULES>")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A program that remove several hashes for a same user. For Responder NetNTLMv2 log file.")
    parser.add_argument("-f","--file", help="File of responder hash to parse.")
    parser.add_argument("-u","--users", default=False, action="store_true", help="Print users parsed from the specified file.")
    parser.add_argument("-uo","--users-only", default=False, dest='users_only', action="store_true", help="Only print users parsed. Do not write output file.")
    parser.add_argument("-m","--machine", default=False, action="store_true", help="Keep the machines NetNTLMv2 hash in the output file. Default these hashes are deleted.")
    parser.add_argument("-o","--output", default="unik-output.txt", help="Output file. Default : unik-output.txt")
    
    args = parser.parse_args()

    if args.file:
        try:
            if exists(args.file):
                reader(args.file, args.output, args.machine, args.users, args.users_only)
            else:
                sys.exit(f"{RED}The specified file{Default} '{args.file}' {RED}was not found.{Default}")
        except Exception as error:
            sys.exit(f"{RED}ERROR :\nException : {error}{Default}")
    else:
        sys.exit(f"{YELLOW}[!] You must specified a NetNTLMv2 file !{Default}\nTry '-h' for the help.")
