'''
#寄送email的程式
#準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg['From']="560628chen@gmail.com"
msg['To']="560628chen@gmail.com"
msg['Subject']="你好阿睿"
#寄送純文字內容
msg.set_content("測試看看")
#寄送多樣式的內容(html)
#msg.add_aiternative("<h3>優惠券</h3>滿五百送一百喔", subtype="html")
#連接到SMTP Server,驗證寄件人身分並發送郵件
import smtplib
#到網路上搜尋gmail smtp server 或是yahoo smtp server
server = smtplib.SMTP('smtp.gmail.com',465)
server.login("560628chen@gmail.com", "qaz2013*")
server.send_message(msg)
server.close()
'''

import smtplib
import email.message

def send_email():
    msg = email.message.EmailMessage()
    msg['From'] = "560628chen@gmail.com"
    msg['To'] = "560628chen@gmail.com"
    msg['Subject'] = "你好阿睿"
    #msg.set_content("測試看看")
    msg.add_alternative("<h3>優惠券</h3>滿五百送一百喔", subtype="html")

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("560628chen@gmail.com", "rkxy prfk kcvf tgur")  # 請將 "your_password" 換成你的 Gmail 密碼或應用程式密碼
        server.send_message(msg)
        server.close()
        print("郵件已成功發送！")
    except smtplib.SMTPServerDisconnected as e:
        print("SMTP 伺服器連接意外關閉。")
        print(e)
    except Exception as e:
        print("發生其他錯誤。")
        print(e)

if __name__ == "__main__":
    send_email()
 