import smtplib

# Convert this to a class model
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mathewshinu9474@gmail.com', 'qhhtfalsdvkacktn')

    subject = 'The price fell down'
    body = 'check the link https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B085J19V4P/ref=lp_22429860031_1_1?s=electronics&ie=UTF8&qid=1606594150&sr=1-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mathewshinu9474@gmail.com',
        'shinu.mathews28@gmail.com',
        msg
    )

    print('Email sent')

    server.quit()

def send_html_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mathewshinu9474@gmail.com', 'qhhtfalsdvkacktn')

    subject = 'The price fell down'
    body = 'check the link https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B085J19V4P/ref=lp_22429860031_1_1?s=electronics&ie=UTF8&qid=1606594150&sr=1-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mathewshinu9474@gmail.com',
        'shinu.mathews28@gmail.com',
        msg
    )

    print('Email sent')

    server.quit()

send_mail()