#!/usr/bin/env python3
"""
Learning about if, elif, and else
"""
channels = [4, 2, 5, 8, 11, 7, 39, 80, 127, 253, 367, -412, 1000]

# sort by package: basic - 1 to 10, premium, 11 to 50, extras 51 - 300
for chan in channels:
    if chan > 0 and chan <= 10:
        print("You want the basic package")
    elif chan <= 50:
        print("You want the premium package")
    elif chan <= 300:
        print("You want the extras package")
    else: 
        print("That's not a valid channel number!")
