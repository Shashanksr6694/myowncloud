
import commands 
commands.getoutput('yum install cifs-utils samba-client')
commands.getoutput('mkdir /media/ankur')
commands.getoutput('mount -o username=ankur//192.168.43.98/ankur /media/ankur')