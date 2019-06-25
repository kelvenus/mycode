#!/usr/bin/env python3
#ipchk = '192.168.0.1'

# Prompt user for the IP address
ipchk = input('Apply an IP address: ') # this line now prompt the user for input

if ipchk == '192.168.70.1': # if a match on '192.168.70.1' data is provided,  this will test truei
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not reccommended.')
elif ipchk: # if any data is provided, this will test true
    print('Looks like the IP address was set: '+ ipchk)
else: # if data is not provided
    print('You did not provide input.') # intended under else


