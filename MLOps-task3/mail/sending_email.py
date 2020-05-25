# Python program for sending email
# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "mayank_var1998@outlook.com"
# Receivers email
rec_email = "89233mayank@gmail.com"

message = """ The Best Model has been created..
              You may further proceed.
              Thank You ! """
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("mayank_var1998@outlook.com", "mayvar1998")
print("Login Success!")
# Send Email
server.sendmail("Mayank Varshney", "89233mayank@gmail.com", message)
print(f"Email has been sent successfully to {rec_email}")
