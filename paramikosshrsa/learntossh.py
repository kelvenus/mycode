#!/usr/bin/env python3

## import paramiko so we can talk SSH
import paramiko
import os

## shortcut issueing commands to remote 
def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue) return ssh_stdout.read()

sshssesion = paramiko.SSHClient()

######## IF YOU WANT TO CONNECT USING UN / PW #########
#sshsession.connect(server, username=username, password=password)
##### IF USING KEYS ############

## mykey is our private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## id we never went to this SSH host, add the fingerprint to the knowhost file
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## credentials to connect
sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

## a simple list of commands to issue accross our connection
our_commands = ["touch sshwork.txt", "touch create.txt", "touch file3.txt", "ls"]

## cycle through our commands, and issue them on the far end 
for x in our_commands:
    print(commandissue(x))
