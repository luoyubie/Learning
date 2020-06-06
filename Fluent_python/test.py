# _*_ coding:utf-8 _*_
# @Author: Bie
# @Time: 2019年03月12日

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.sina.com"  # 设置服务器
mail_user = "luoyu_bie@sina.com"  # 用户名
mail_pass = "8de9ab1243cca6bd"  # 口令

sender = 'luoyu_bie@sina.com'
receivers = ['185398921@qq.com',]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(mail_user)
message['To'] = Header("python email", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")



