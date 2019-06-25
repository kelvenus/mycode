#!/usr/bin/env python3

# Create host list
hosts = [{"server": "North", "ip": "10.1.2.3"},{"server": "South", "ip": "10.4.5.6"},{"server": "West", "ip": "10.7.8.9"}]

print('The first server is: {0}\
       The second server is: {1}\
       The third Server is: {2}'.format(hosts[2]["server"]), hosts[2]["ip"])
hosts.append({"server": "East", "ip": "10.10.11.12"})
print(hosts[0]["server"], hosts[0]["ip"])
print(hosts[3]["server"], hosts[3]["ip"])

