
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Thread

your_email = "tankmansodari.073@kathford.edu.np"
email_to = "tankamansodari7@gmail.com"
password = "sseccus@tankmans"
subject = "Ekbana Temperature Report"
text = """\
    Hi,
    Your device temperature is getting Down.do something"""


class EmailThread(Thread):
    def __init__(self, ):
        Thread.__init__(self)

    def run (self):
        text = "Mail form ekbana"
        message = MIMEMultipart("alternative")
        message["Subject"] = "Alert Alert Alert" 
        message["From"] = "your@email.com"
        message["To"] = email_to
        part1 = MIMEText(text, "plain")
        message.attach(part1)
    
        context = ssl.create_default_context()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(your_email, password)
            server.sendmail(your_email, email_to, message.as_string())
    def hello():
        print("hello world")

# EmailThread().start()
# EmailThread.hello()