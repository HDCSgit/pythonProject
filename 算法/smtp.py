#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import xlrd

# 读取excel.xls的行内容列表
def email_address():
    elist=[]
    work_book = xlrd.open_workbook('email.xls')
    sheet1 = work_book.sheet_by_name('Sheet1')
    cellVallues = sheet1.get_rows()
    for cellVallue in cellVallues:
        for cell in cellVallue:
            if cell.value != 'email':
                elist.append(cell.value)
    return elist

# 邮箱字符串
def email_address_str(num):
    elist = email_address()
    email = ''.join(elist[num])
    return email



"""

from_addr='121044473@qq.com'   #邮件发送账号
to_addrs='1244716205@qq.com'   #接收邮件账号
qqCode='dzowlvlyqbjmbgid'   #授权码（这个要填自己获取到的）
smtp_server='smtp.qq.com'#固定写死
smtp_port=465#固定端口


#配置服务器
stmp=smtplib.SMTP_SSL(smtp_server,smtp_port)
stmp.login(from_addr,qqCode)

#组装发送内容
message = MIMEText('我是发送的内容', 'plain', 'utf-8')   #发送的内容
message['From'] = Header("Python邮件预警系统", 'utf-8')   #发件人
message['To'] = Header("管理员", 'utf-8')   #收件人
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')  #邮件标题

try:
    stmp.sendmail(from_addr, to_addrs, message.as_string())
except Exception as e:
    print ('邮件发送失败--' + str(e))

print ('邮件发送成功')
"""