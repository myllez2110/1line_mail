import argparse
from email_sender import EmailSender  

def main():
    parser = argparse.ArgumentParser(description='Enviar um email através da linha de comando.')
    parser.add_argument('-u', '--user', required=True, help='Email do usuário')
    parser.add_argument('-p', '--password', required=True, help='Senha do email do usuário')
    parser.add_argument('-t', '--to', required=True, help='Email do destinatário')
    parser.add_argument('-s', '--subject', required=True, help='Assunto do email')
    parser.add_argument('-c', '--content', required=True, help='Conteúdo do email')

    args = parser.parse_args()

    email_sender = EmailSender(args.user, args.password)
    email_sender.send_email(args.to, args.subject, args.content)

if __name__ == '__main__':
    main()
