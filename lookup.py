#!/usr/bin/env python3
import ipaddress
import socket
import asyncio
import sys
import os.path


async def lookup(loop, addresses, max_length=None):
    ''' loop: asyncio event loop
    addresses: list of ip address or hostnames
    max_length: spacer width of first print column
    prints address and its corresponding ip or hostname
    '''
    for address in addresses:
        address = address.strip()
        try:
            ipaddress.ip_address(address)
            lookup = await loop.getnameinfo((address, 80))
            lookup = lookup[0]
        except ValueError:
            try:
                lookup = await loop.getaddrinfo(
                    host=address,
                    port=80,
                    proto=socket.IPPROTO_TCP
                )
                lookup = lookup[0][4][0]
            except socket.gaierror as e:
                lookup = f'EXCEPTION: {e}'

        print(f'{address:{max_length}} {lookup}')


def lookup_loop(addresses, max_length=None):
    ''' addresses: list of ip addresses or hostnames
    max_length: spacer width of first print column
    async lookup wrapper
    '''
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(lookup(loop, addresses, max_length))
    finally:
        loop.close()


def main():
    ''' reads input passed in
    prints how to use if no args passed in
    if first input is a file, then run lookup on each line of file
    otherwise, run lookup on arguments
    prints a list of addresses and their corresponding ip address or hostname
    '''
    if len(sys.argv) == 1:
        self = sys.argv[0]
        divider = '-' * 60
        ARG_EXCEPTION = f'''
{divider}

Prints corresponding ip or hostname of input

USAGE:
    {self} <file of ips or hostnames on each line>

        -- or --

    {self} <list of ips or hostnames. space delimited>

{divider}
        '''
        print(ARG_EXCEPTION)
    elif os.path.isfile(sys.argv[1]):
        addresses = open(sys.argv[1]).readlines()
        max_length = len(max(open(sys.argv[1], 'r'), key=len))
        lookup_loop(addresses, max_length=max_length)
    else:
        addresses = sys.argv[1:]
        max_length = len(max(addresses, key=len))
        lookup_loop(addresses, max_length=max_length)


if __name__ == '__main__':
    main()
