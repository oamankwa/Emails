from flask import Flask
import ssl
import smtplib
from messageText import Createmessage
from attach import Attachment


app = Flask(__name__)

# set up your variables
Host = 'smtp.gmail.com' # when using gmail server
Port = 465
Email_Sender = 'youremailaddress@gmail.com' 
Email_Password = 'yourpassword' # This has to be created by following this link below for gmail
Subject = 'Testing Email'
Body = 'I am testing my new email'
From_email = 'youremailaddress@gmail.com'
To_email = 'yourtoemailaddress@gmail.com'

# write your email massage
mymessage = Createmessage(Subject, Body)
msg = mymessage.write_email()

#attach files to message
mylist = ['newexcell.xlsx', 'picture.jpg', 'newtext.txt', 'yourresume.pdf']
myattachment = Attachment(mylist)
myattachment.attech('application','octet-stream',msg)
context = ssl.create_default_context()

# send email
with smtplib.SMTP_SSL(Host, Port, context=context) as smtp:
    smtp.login(Email_Sender, Email_Password)
    smtp.sendmail(From_email, To_email, msg.as_string())
smpt.quit()



    

    

if __name__ == "__main__":
  app.run(debug=True)
