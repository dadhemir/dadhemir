import smtplib
from email.message import EmailMessage

# This is the big problem....OMG !!!
user='ncpedrazac@bucaramanga.gov.co'
password = 'Cc63451225'
smtpsrv = "smtp.office365.com"

#
smtpserver = smtplib.SMTP(smtpsrv,587)
msg = EmailMessage()
#
msg['Subject'] = 'Información importante sobre vinculación'
msg['From'] = 'Alcaldía de Bucaramanga <ncpedrazac@bucaramanga.gov.co>'
msg['To'] = 'dadhemir@gmail.com'

smtpserver.starttls()
smtpserver.login(user, password)
smtpserver.send_message(msg)
smtpserver.close()