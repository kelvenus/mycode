#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""
# Replace the below with ainnow generated URL

LOOKUPAPI ='https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=07111&date=2019-09-17&distance=25&API_KEY=97D5936F-771E-42D9-ACA9-9898CC3A81F1'

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the methods available to our new object
    print(r.json())

main()
