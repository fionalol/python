#!/usr/bin/python

import smtplib

def sendMsg(from_addr,to_addrs,msg):
    mailbox=smtplib.SMTP(host='10.17.224.23', port=2025) 
    mailbox.set_debuglevel(1)
    mailbox.ehlo()
    mailbox.sendmail(from_addr, to_addrs, msg)
    mailbox.quit()

from_addr='a1@openwave.com'
to_addrs='b1@openwave.com'
msg='''from:hello@openwave.com\n
to:test@openwave.com\n
subject:oiioio\n'''
sendMsg(from_addr, to_addrs, msg)
