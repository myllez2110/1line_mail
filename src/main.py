import argparse
from email_sender import EmailSender  

def main():
    parser = argparse.ArgumentParser(
        description="Command-line email sender script with optional file attachment."
    )

    parser.add_argument(
        '-u', '--user',
        required=True,
        help='The sender email address. Example: user@gmail.com'
    )

    parser.add_argument(
        '-p', '--password',
        required=True,
        help="The password or app-specific password for the sender's email account."
    )

    parser.add_argument(
        '-t', '--to',
        required=True,
        help="The recipient's email address. Example: recipient@example.com"
    )

    parser.add_argument(
        '-s', '--subject',
        required=True,
        help="The subject of the email."
    )

    parser.add_argument(
        '-c', '--content',
        required=True,
        help="The body content of the email. This will be included as plain text."
    )

    parser.add_argument(
        '-a', '--attachment',
        required=False,
        help="Optional: File path to a file you want to attach to the email. Example: '/path/to/file.txt'"
    )

    args = parser.parse_args()

    email_sender = EmailSender(args.user, args.password)
    email_sender.send_email(args.to, args.subject, args.content, args.attachment)

if __name__ == '__main__':
    main()
