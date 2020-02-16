from email.mime.text import MIMEText
from smtplib import SMTPException
import time

class Mail():
    '''
    构造mail实体内容
    '''
    def __init__(self,server=None,to_addr=None):
        self._server=server
        self._to_addr=to_addr
        self._title='Empty title'
        self._content='Hi,this is mail content'

    @property
    def mail_title(self):
        return self._title

    @mail_title.setter
    def mail_title(self,title):
        self._title=title

    @property
    def mail_content(self):
        return self._content

    @mail_content.setter
    def mail_content(self,content):
        self._content=content

    def send_mail(self):
        cur_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime())
        try:
            msg = MIMEText(self.mail_content, 'plain', 'utf-8')
            msg['From'] = self._server.from_addr
            msg['To'] = ';'.join(self._to_addr)
            msg['Subject'] = cur_time+'  '+self._title
            self._server.smtp_sever.sendmail(self._server.from_addr, self._to_addr, msg.as_string())

            print ('{}:From {} to {} send successfully'.format(cur_time,self._server.from_addr,self._to_addr))
        except SMTPException as e:
            print (e)
            print('{}:From {} to {} send failed'.format(cur_time,self._server.from_addr, self._to_addr))