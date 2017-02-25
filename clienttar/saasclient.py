#!/usr/bin/python2 
import os 
os.system("yum install openssh-clients") 
os.system("systemctl restart sshd")
os.system("ssh  -X ankur@192.168.43.98 firefox") 