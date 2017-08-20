from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr='13023256824@163.com'
password='mxf081233'
to_addr='997150276@qq.com'

smtp_server='smtp.163.com'

msg=MIMEText('爬虫异常','plain','utf-8')
msg['From']=_format_addr('一号爬虫<{}>'.format(from_addr))
msg['To']=_format_addr('管理员<{}>'.format(to_addr))
msg['Subject']=Header('一号爬虫运行状态','utf-8')

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()