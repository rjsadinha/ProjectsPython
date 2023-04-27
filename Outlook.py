import win32com.client as win32

#criar a integraão 
webmail = win32.Dispatch('oulook.Application')

# Criar um email 
email = outlook.CreateItem(0)

# configurar as informamcoes do se email
email.To = "destino"
email.Subject = "assunto"
email.HTMLBody = "corpor do email" """ Ola lucca aqui e o email"""

email.Send()
print("email enviado")
