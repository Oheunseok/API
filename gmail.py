import smtplib
from email.mime.text import MIMEText

loginID,loginPW="shin1sub2@gmail.com","2fjsrjtehhag" #GMAIL ID,PW

# "shin1sub2@gmail.com"
senderAddr ="secretfice@naver.com" #반영이 안됨
recipientAddr = "ssuby11@naver.com"
text = "본문 샬라샬라"


msg = MIMEText(text,_charset="utf8")
msg['Subject'] = "api 발송 메일"  #제목
msg['From'] = senderAddr            #발신자
msg['to'] = recipientAddr           #수신자



s=smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(loginID,loginPW)
s.sendmail(senderAddr,recipientAddr,msg.as_string())


s.quit()