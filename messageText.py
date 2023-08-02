from flask import Flask 
from email.message import EmailMessage

#create a test message to be uesd in sending email
class Createmessage:

    #create variables
    SUBJECT = ''
    BODY = ''
 

    #Add a constructor
    def __init__(self, subject, body):
        self.SUBJECT = subject
        self.BODY = body
     

    #Write an  email 
    def write_email(self from_email, to_email):
        msg = EmailMessage()
        msg['Subject'] = self.SUBJECT
        msg['from'] = from_email
        msg['to'] = to_email
        msg.set_content(self.BODY)
        return msg
        

