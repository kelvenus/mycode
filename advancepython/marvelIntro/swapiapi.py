#!/usr/bin/env python3

# imports always go at the top of your code
import requests

# Replace the below with ainnow generated URL
#LOOKUPAPI ='https://swapi.co/api/people/1/?format=json'

for i in range(1, 16):
    r = requests.get(f'https://swapi.co/api/people/{i}/?format=json')
# imports always go at the top of your code
    data = r.json()

     ## set up screen
    print("Practicing Using Request API")
    print("----------------")
    print(f'{data["name"]} is {data["hair_color"]}')
main()
