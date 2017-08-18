#!/usr/bin/env python3
import socket
import asyncio
import sys
import os.path


async def lookup(address):
    ''' address: ip addresses or hostnames
    returns corresponding ip address or hostname of given address
    '''
    try:
        socket.inet_aton(address)
        hostname = socket.gethostbyaddr(address)
        return hostname[0]
    except socket.error:
        ip = socket.gethostbyname(address)
        return ip


def lookup_loop(addresses):
    ''' addresses: list of ip addresses or hostnames
    returns a list of corresponding ip address or hostname for a given address
    '''
    loop = asyncio.get_event_loop()
    requests = [
        asyncio.ensure_future(lookup(address.strip())) for address in addresses
    ]

    try:
        return loop.run_until_complete(asyncio.gather(*requests))
    finally:
        loop.close()


def main():
    ''' reads first input passed to script
    if input is a file, then run lookup on each line of file
    otherwise, run lookup on input
    prints a list of addresses and their corresponding ip address or hostname
    '''
    if os.path.isfile(sys.argv[1]):
        addresses = open(sys.argv[1]).readlines()
        max_length = len(max(open(sys.argv[1], 'r'), key=len))
        lookups = lookup_loop(addresses)
        for pair in list(zip(addresses, lookups)):
            addr1, addr2 = pair
            print(f'{addr1.strip():{max_length}} {addr2}')
    else:
        addr = lookup_loop([sys.argv[1].strip()])[0]
        print(f'{sys.argv[1]} {addr}')


if __name__ == '__main__':
    main()
