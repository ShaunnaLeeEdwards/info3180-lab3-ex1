import smtplib

from_name =  "SLE"

to_name = "LES"

from_addr = "myemailaddress@gmail.com"

to_addr = "yourmailaddress@gmail.com"

subject = "Final Year At UWI"

msg = "Make the most of this year! Afterall, it's final year!"


message = """From: {} <{}>

To: {} <{}> 

Subject: {}

{}

"""
message_to_send = message.format(from_name, from_addr, to_name,
 
 to_addr, subject, msg)

# Credentials (if needed)

username = "myemailaddress@gmail.com"

password = "myappcode"

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username, password)

server.sendmail(from_addr, to_addr, message_to_send)

server.quit() 