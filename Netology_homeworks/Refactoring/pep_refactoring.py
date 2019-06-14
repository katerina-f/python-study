import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


YANDEX_SMTP = "smtp.yandex.ru"
YANDEX_IMAP = "imap.yandex.ru"

def main():
    login = 'login@yandex.ru'
    password = 'password'
    subject = 'Subject'
    recipients = ['login@gmail.com']
    message = 'Message'
    header = None

    my_mail = Postman(login, password,
                subject, recipients, message,
                header)
    my_mail.send_message()
    my_mail.recieve_message()


class Postman:
    def __init__(self, login, password, subject,
                recipients, message,header=None):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send_message(self):
        message_obj = MIMEMultipart()
        message_obj['From'] = self.login
        message_obj['To'] = ', '.join(self.recipients)
        message_obj['Subject'] = self.subject
        message_obj.attach(MIMEText(self.message))

        smtp_obj = smtplib.SMTP(YANDEX_SMTP, 587)
        # identify ourselves to smtp gmail client
        smtp_obj.ehlo()
        # secure our email with tls encryption
        smtp_obj.starttls()
        # re-identify ourselves as an encrypted connection
        smtp_obj.ehlo()
        smtp_obj.login(self.login, self.password)
        smtp_obj.sendmail(self.login, self.recipients, message_obj.as_string())
        smtp_obj.quit()

    def recieve_message(self):
        message_obj = imaplib.IMAP4_SSL(YANDEX_IMAP)
        message_obj.login(self.login, self.password)
        message_obj.list()
        message_obj.select("inbox")
        criterion = f'(HEADER Subject "{self.header}")' if self.header else 'ALL'
        result, data = message_obj.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = message_obj.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        print(email_message)
        message_obj.logout()


if __name__ == '__main__':
    main()
