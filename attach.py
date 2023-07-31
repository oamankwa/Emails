from flask import Flask
#from email.message import EmailMessage
import os

class Attachment:

    ATTACHMENT = []

    #Add constructor
    def __init__(self, attachment):
        self.ATTACHMENT = attachment

       
       
    #Gets the list of attachments loops through it reads and get the filenames and attach them to the message
    def attech(self, maintype, subtype, msg):
        files = self.ATTACHMENT
       
        for file in files:
            file_type = file.split('.')
            file_type = file_type[0]
            if file_type == 'JPG' or file_type == 'jpg' or file_type == 'PNG' or file_type =='png':
                import imghdr
                with open(file, 'rb') as f:
                    file_data = f.read()
                    image_type = imghdr.what(file)
                msg.add_attachment(file_data, maintype='image', subtype=image_type, filename= file_name)
            else:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
                msg.add_attachment(file_data, maintype = maintype, subtype = subtype, filename = file_name)



    


    