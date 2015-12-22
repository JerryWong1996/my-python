# -*- coding: utf-8 -*-
#写一封邮件

from email import encoders
from email.mime.text import MIMEText
from email.header import header
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((\
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input("From: ")
password = raw_input("Password: ")
smtp_server = raw_input("SMTP server:")
to_addr = raw_input("To: ")

msg = MIMEText('Hello, world! Send by python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr(u'管理者<%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候.....', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(0)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()