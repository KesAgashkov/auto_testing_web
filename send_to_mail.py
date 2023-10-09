import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from time import sleep

sleep(10)
fromaddr = "адрес куда отправить"
toaddr = "адрес кому отправить"
mypass = "В этом месте указан пароль для внешний приложений"
log = "log.txt"
report_api = "report_api.html"
report_gui = "report_gui.html"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от Костяна"
text = "Hello"

msg.attach(MIMEText(text))

with open(log, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(log))
    part['Content-Disposition'] = f'attachment; filename="{basename(log)}"'
    msg.attach(part)

with open(report_api, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(report_api))
    part['Content-Disposition'] = f'attachment; filename="{basename(report_api)}"'
    msg.attach(part)

with open(report_gui, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(report_gui))
    part['Content-Disposition'] = f'attachment; filename="{basename(report_gui)}"'
    msg.attach(part)


server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
