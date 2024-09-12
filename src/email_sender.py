from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import os

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

    def send_email(self, receiver_email, subject, body, attachment_path=None):
        if self.smtp_server is None:
            print("Non-supported e-mail.")
            return
        
        # Setting up the message
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        # Attach the body of the email.
        message.attach(MIMEText(body, 'plain'))

        # Attach the file if specified
        if attachment_path:
            try:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={os.path.basename(attachment_path)}",
                    )
                    message.attach(part)
            except Exception as e:
                print(f"Error attaching file: {e}")
                return

        #Sending the email
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # TLS connection starts

            server.login(self.sender_email, self.sender_password)

            server.sendmail(self.sender_email, receiver_email, message.as_string())

            print("Email sent successfully!")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            server.quit()
