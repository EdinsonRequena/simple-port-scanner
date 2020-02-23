#!/bin/python3.8

import sys, socket
from datetime import datetime as dt

target = None

def scanner():
    global target

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Invalid amount of arguments.")
        sys.exit()


def cli():
    global start_port, final_port

    print('-' * 50)
    print('Scaning target '+target)
    print('Time started: '+str(dt.now()))
    print('-' * 50)

    start_port = int(input('Choose the start port: '))
    final_port = int(input('Choose the final port: '))


def try_except():

    try:
        for ports in range(start_port, final_port):
            skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = skt.connect_ex((target, ports))
            print(f'Port {ports}')
            if result == 0:
                print(f'Port {ports} is open')
                s.close()

    except KeyboardInterrupt:
        print('\nEnding program.')
        sys.exit()

    except socket.gaierror:
        print('Invalid hostname')
        sys.exit()

    except socket.error:
        print("Could't connet to server, check your internet connection.")
        sys.exit()

if __name__ == '__main__':
    scanner()
    cli()
    try_except()
