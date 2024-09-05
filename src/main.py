import argparse
from email_sender import EmailSender  

def main():
    parser = argparse.ArgumentParser(description='1 line command email sender')
    parser.add_argument('-u', '--user', required=True, help='user email')
    parser.add_argument('-p', '--password', required=True, help='user password email')
    parser.add_argument('-t', '--to', required=True, help='email to send')
    parser.add_argument('-s', '--subject', required=True, help='Subject')
    parser.add_argument('-c', '--content', required=True, help='Content')

    args = parser.parse_args()

    email_sender = EmailSender(args.user, args.password)
    email_sender.send_email(args.to, args.subject, args.content)

if __name__ == '__main__':
    main()
