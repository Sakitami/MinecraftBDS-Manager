import os
import configparser
from sshconnect import sshconnect

ssh = configparser.ConfigParser()
ssh.read('ssh.cfg')
ssh_remote = ssh.items('SSH')
os.system('sshpass -p '+ssh_remote[3][1]+' scp build-shell/build-debian10.sh '+ssh_remote[2][1]+'@'+ssh_remote[0][1]+':/root/build-debian10.sh')
command = ['cd /root', 'chmod +x build-debian10.sh', './build-debian10.sh']
sshconnect(ssh_remote[0][1], ssh_remote[1][1], ssh_remote[2][1], ssh_remote[3][1], command)