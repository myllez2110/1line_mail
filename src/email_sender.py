
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server, self.smtp_port = self.get_smtp_server(sender_email)

    def get_smtp_server(self, email):
        domains = {
            'gmail.com': ('smtp.gmail.com', 587),
            'outlook.com': ('smtp.office365.com', 587),
            'yahoo.com': ('smtp.mail.yahoo.com', 587),
            'mail.com': ('smtp.mail.com', 587),
            'aol.com': ('smtp.aol.com', 587),
        }
        
        domain = email.split('@')[-1]
        return domains.get(domain, (None, None))

    def send_email(self, receiver_email, subject, body):
        if self.smtp_server is None:
            print("Non supported e-mail.")
            return
        
        # Setting up the message
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        # Attach the body of the email.
        message.attach(MIMEText(body, 'plain'))

        # Sending the email
        try:
            # Connection to the smtp server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # LTS connection starts

            server.login(self.sender_email, self.sender_password)

            server.sendmail(self.sender_email, receiver_email, message.as_string())

            print("Email sent successfully!")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            server.quit()
    
    #def spam_email(self, receiver_email, subject, body, num):
     #   i = 0
      #  while(i < num):
       #     EmailSender.send_email(self, receiver_email, subject, body)
        #    i = i + 1
         #it's just an idea for now, probably wont make it to final.   
