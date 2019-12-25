import smtplib
from time import strftime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
class SendEmail():
    def __init__(self,server= 'smtp.126.com',user='my_dsd@126.com',password='mydsdqaz123',sender='my_dsd@126.com',path=None):
        # 发送邮件服务器
        self.smtpserver = server
        # 发送邮箱用户名和密码
        self.user = user
        self.password = password
        # 发送邮箱
        self.sender = sender
        # 接受邮箱
        self.receiver = ['dushundong@mail.dataoke.com','chenquanjun@mail.dataoke.com','dongbenjian@mail.dataoke.com','tanghao@mail.dataoke.com','wangliang@mail.dataoke.com']
        # 创建一个带附件的实例
        self.message = MIMEMultipart()
        '''From与To与sendmail保持一致'''
        self.message['From'] = self.sender
        self.message['To'] = ";".join(self.receiver)
        now_time = strftime('%Y-%m-%d %H:%M:%S')
        subject = '接口报告{}'.format(now_time)
        self.message['Subject'] = Header(subject, 'utf-8')
        self.message['Date'] = Header('{}'.format(now_time), 'utf-8')
        self.message.attach(MIMEText('接口报告%s'%now_time, 'plain', 'utf-8'))
        # 构造附件，传送指定目录下的测试报告
        with open(path,"rb") as file:
            mail_body = file.read()
        att= MIMEText(mail_body, 'html', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        #这里的filename可以任意写，写什么名字 邮件中就显示什么名字
        att['Content-Disposition'] = 'attachment;filename:"api_report.html"'
        self.message.attach(att)
    def send_email(self):
        with smtplib.SMTP() as smtp:
            smtp.connect(self.smtpserver, 25)
            smtp.login(self.user, self.password)
            smtp.sendmail(self.sender, ";".join(self.receiver), self.message.as_string())
            print("发送邮件成功！请前往【%s】邮箱查看！"%(";".join(self.receiver)))
if __name__ == '__main__':
    send = SendEmail(path=r"D:\report\wap_product_report201808311117.html")
    send.send_email()