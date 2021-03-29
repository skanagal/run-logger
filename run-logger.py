#!/usr/bin/python
import subprocess as proc
import syslog
import sys
syslog.syslog(syslog.LOG_INFO | syslog.LOG_LOCAL4,sys.argv[1]+' '+' Started collecting output.')
# try:
#     myout=proc.check_output("FastCli -p 15 -c '%s > flash:mytech.txt'"%sys.argv[2], shell=True)
#     syslog.syslog(syslog.LOG_INFO | syslog.LOG_LOCAL4,sys.argv[1]+' '+' Finished collecting the output.')
# except:
#     syslog.syslog(syslog.LOG_INFO | syslog.LOG_LOCAL4,sys.argv[1]+' '+' The command failed. Pls try again.')

try:
    myout=proc.check_output("FastCli -p 15 -c show %s route vrf vrf-internet > flash:bgp-routes-%s.txt"%(sys.argv[2],sys.argv[2]), shell=True)
    syslog.syslog(syslog.LOG_INFO | syslog.LOG_LOCAL4,sys.argv[1]+' '+' Finished collecting the output.')
except:
    syslog.syslog(syslog.LOG_INFO | syslog.LOG_LOCAL4,sys.argv[1]+' '+' The command failed. Pls try again.')
