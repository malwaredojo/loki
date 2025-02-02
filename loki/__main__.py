#! /usr/bin/env python3
"""
Entrypoint
"""
from loki.loki import *

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting...')
