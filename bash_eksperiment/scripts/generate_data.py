#!/usr/bin/env python3

"""
Genereerib 200 juhuslikku täisarvu vahemikus 1 kuni 100.
"""

import random

def main():

    for _ in range(200):
        number = random.randint(1, 100)
        print(number)

if __name__ == "__main__":
    main()
