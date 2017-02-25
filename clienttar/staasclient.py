
 import commands
commands.getoutput('yum install fuse-sshfs')
commands.getoutp('systemctl restart sshfs')
commands.getoutput('systemctl restart sshd')
commands.getoutput('mkdir /root/Desktop/navjot ')
 commands.getoutput('sshfs navjot@192.168.43.98:/navjot /root/Desktop/navjot ') 
 