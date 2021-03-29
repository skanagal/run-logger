import paramiko
import sys
def push_cmd(ssh,CMD):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(CMD)

def get_output(ssh,CMD):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(CMD)
    for line in ssh_stdout:
        print (line.strip('\n'))

def main():
    ssh = paramiko.SSHClient()
    SWITCH='172.30.154.65'
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(SWITCH, username='admin', password='admin')
    # get_output(ssh,'show version')
    # push_cmd(ssh," alias field_set_refresh bash setsid python /mnt/flash/run-logger.py %1 %2")
    push_cmd(ssh,"configure terminal\nalias field_set_refresh bash setsid python /mnt/flash/run-logger.py %1 %2")
    push_cmd(ssh,"field_set_refresh "+sys.argv[1]+' '+sys.argv[2])

    # print "field_set_refresh "+sys.argv[1]+' '+sys.argv[2]
    # push_cmd(ssh,"bash setsid  python /mnt/flash/run-logger.py 443 'show tech-support'")
    ssh.close()
main()
