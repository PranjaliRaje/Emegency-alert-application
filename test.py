import smtplib

gmail_user = 'sjalerts.app@gmail.com'  
gmail_pwd = 'rootroot'

sent_from = gmail_user  
to = ['pranjaliraje@gmail.com'] 
subject = 'OMG Super Important Message'  
body = 'Hey, what'



try:  
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + ", ".join(to) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + subject + ' \n'
    msg = header + '\n' + body + '\n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')