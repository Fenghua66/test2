import smtplib
from email.message import EmailMessage
# Send the message via SMTP server.

msg = """From: cloudera_notifications@moelis.com>
To: fenghua.liu@moelis.com
Subject: SMTP e-mail test

This is a test e-mail message.
"""

host = 'us-smtp-outbound-1.mimecast.com'
port = '587'
username = 'cloudera_notifications@moelis.com'
password = '#Nv&PmH7NQck5hagenu4gApHjbZYbZg'

sender = 'cloudera_notifications@moelis.com'
receiver = 'fenghua.liu@moelis.com'

with smtplib.SMTP(host, port) as server:
    server.ehlo()  # send the extended hello to our server
    server.starttls()  # tell server we want to communicate with TLS encryption
    
    server.login(username, password)
    server.sendmail(sender, receiver, msg)
    print("Successfully sent email")

    
    


