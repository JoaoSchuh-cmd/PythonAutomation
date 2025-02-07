import smtplib
import ssl 
from email.message import EmailMessage

# Email setup
smtp_server = 'smtp.gmail.com'
port = 465
sender_email = 'joao.schuh@edu.unipar.br'
receiver_email = 'joaoschuh05@gmail.com'
password = 'fhut ccsv gped tjgu'

# Create message
msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Here is your PDF"
msg.set_content("Please find attached the PDF file.")

# Attach PDF
pdf_path = 'C:/Users/JoaoSchuh/Desktop/DirecaoDefensiva.pdf'
with open(pdf_path, 'rb') as f:
    msg.add_attachment(f.read(), maintype = 'application', subtype = 'pdf', filename = 'DirecaoDefensivaFile.pdf')
    
# # Send email
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print("Authentication error:", e)
except Exception as e:
    print("An error occurred:", e)