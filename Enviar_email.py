import smtplib
from email.mime.text import MIMEText

# De quem vai envio e quem vai reveber
de = 'meuEmail@gmail.com'
para = ['outroEmail@gmail.com', 'Maisum@gmail.com']

# Criação da mensagem
msg = MIMEText(''' 

<p>Qual quer coisa aqui<p/>
<p>com formatação em html<p/>

''', 'html', 'utf-8')
msg['From'] = de
msg['To'] = ', '.join(para)
msg['Subject'] = 'Assunto do email'

# Configuração para enviar a mensagem
raw = msg.as_string()
smtp = smtplib.SMPT_SSL('smtp.gmail.com', 465)
smtp.login( de, 'Senha_Conta' )
smtp.sendmail(de, para, raw)
smtp.quit()

# Mensagem enviada
