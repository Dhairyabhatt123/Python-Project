import smtplib as s

# server
ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("dhairyabhatt3110@gmail.com","i will win")
subject = "test python by email cos i love it"
body = "its fun out here!!"
massage = f"{subject} and {body}"
listadd = ['devansh.dp2004@gmail.com']
ob.sendmail('dhairyabhatt3110@gmail.com',listadd,massage)
print("mail sent")
ob.quit()