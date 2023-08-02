# Objects to send emails from the server

Three seperate objects are used in various ways to send emails by server

With these objects the server can send emails using smtp protocal. Always creating individual email code for various applications is difficult, and these objects hides all the details and can be reuse when needed. There are three objects for sending emails, and they are seperated to avoid tight coupling. The objective is that some emails are text and others are html, also emails can be sent with attachment and others don't need attachments.  

To send an email by text the object Createmessage from messageText.py is use. This class imports EmailMessage from email.message and is instaniate with the subject and body of the email. It has only one method write_email which instaniate the EmailMessage model to msg and it calls its msg.subject variable and store the Createmessage subject in it. The 'to' and 'from' parameters are stored in msg variables. Also, msg.set_content method takes the Createmessage body as a parameter.

Html emails are send ny the object Createhtmlmessage from messageHtml.py. This class imports EmailMessage from email.message and is instaniate with the subject and body of the email. It has only one method write_email which instaniate the EmailMessage model to msg and it calls its msg.subject variable and store the Createhtmlmessage subject in it. The 'to' and 'from' parameters are stored in msg variables. Also, msg.add_alternative method takes the Createhtmlmessage body as a parameter.



**Features**

**How to use**

**Links**
