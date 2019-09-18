#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import argparse

#call parser
parser = argparse.ArgumentParser()

def main():
    r = requests.get(f'https://swapi.co/api/people/1/?format=json')
# imports always go at the top of your code
    data = r.json()

     ## set up screen
    print("Practicing Using Request API")
    print("----------------")
    print(f'{data["name"]} is {data["hair_color"]}')

# Add argparse optional argument
    parser.add_argument('--attr', help='')
    args = parser.parse_args()
main()
