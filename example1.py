import smtplib
from email.message import EmailMessage
import imghdr

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

message["Subject"] = "이것은 제목입니다."
message["From"] = "comingtrue910726@gmail.com"
message["To"] = "comingtrue910726@gmail.com"

with open("cake.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('cake',image_file)
print(image_type)
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("comingtrue910726@gmail.com","rnfkwmf!8")
#smtp.send_message(message)
smtp.quit()
