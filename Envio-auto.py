import smtplib
import email.message
from Segredos import senha

def enviar_email():  
    corpo_email =  """
    <p  style="color: aqua;">Vai trabalha vagabundo, deu de ver serie </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Planilha de relatório diário Lucca"
    msg['From'] = 'gvictu8@gmail.com'
    msg['To'] = 'a.damasceno@tjrs.jus.br'
    password = ''
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()