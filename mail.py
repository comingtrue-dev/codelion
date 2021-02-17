import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    #정규표현식
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("코드라이언 수업중이에요")

message["Subject"] = "이것은 제목입니다."
message["From"] = "comingtrue910726@gmail.com"
message["To"] = "comingtrue910726@gmail.com"

#image = open("favicon.ico","rb")
#print(image.read())

with open("cake.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('cake',image_file)
#print(image_type)
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("comingtrue910726@gmail.com","rnfkwmf!8")
sendEmail("comingtrue910726@gmail.com")
smtp.quit()
