from smtplib import SMTP_SSL
from config.config import *


class Server():

    def __init__(self,server_name=SMTP_SERVER,passwd=PASSWORD,
                 from_addr=FROM_ADDR,debug=False):
        self.smtp_sever=SMTP_SSL(SMTP_SERVER)
        self.passwd=passwd
        self.from_addr=from_addr
        self.smtp_sever.set_debuglevel(debug)

    def connet(self):
        try:
            self.smtp_sever.ehlo(SMTP_SERVER)
            self.smtp_sever.login(self.from_addr,self.passwd)
            return True
        except SMTPException as e :
            print ('login failed')
            return False

    def close(self):
        self.smtp_sever.quit()