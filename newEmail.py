# This file is use to test sending emails and attaching files  
from flask import Flask
import ssl
import smtplib
from messageText import Createmessage
from attach import Attachment


app = Flask(__name__)

Host = 'smtp.gmail.com'
Port = 465
Email_Sender = 'yoursender.com' 
Email_Password = 'yourpassword'
Subject = 'Testing Email'
Body = 'I am testing my new email'
From_email = 'youraddress@gmail.com'
To_email = 'tomail@gmail.com'



mymessage = Createmessage(Subject, Body)
msg = mymessage.write_email()

#attach file to message
mylist = ['newexcell.xlsx', 'edward.jpg', 'newtext.txt', 'Resume.pdf']
myattachment = Attachment(mylist)
myattachment.attech('application','octet-stream',msg)
context = ssl.create_default_context()

with smtplib.SMTP_SSL(Host, Port, context=context) as smtp:
    smtp.login(Email_Sender, Email_Password)
    smtp.sendmail(From_email, To_email, msg.as_string())



    

    

if __name__ == "__main__":
  app.run(debug=True)
