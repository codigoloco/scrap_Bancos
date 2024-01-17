import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuración del correo electrónico
remitente = 'tu_correo@gmail.com'
destinatario = 'destinatario@gmail.com'
asunto = 'Asunto del correo'
cuerpo = 'Cuerpo del correo'

# Creación del objeto mensaje
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto

# Agregar el cuerpo del correo
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Adjuntar el archivo
ruta_archivo = 'ruta/al/archivo'
archivo = open(ruta_archivo, 'rb')
parte_adjunta = MIMEBase('application', 'octet-stream')
parte_adjunta.set_payload((archivo).read())
encoders.encode_base64(parte_adjunta)
parte_adjunta.add_header('Content-Disposition', "attachment; filename= %s" % ruta_archivo.split('/')[-1])
mensaje.attach(parte_adjunta)

# Conexión al servidor SMTP de Gmail
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()

# Inicio de sesión en el servidor SMTP de Gmail
servidor.login(remitente, 'tu_contraseña')

# Envío del correo electrónico
servidor.sendmail(remitente, destinatario, mensaje.as_string())

# Cierre de la conexión con el servidor SMTP de Gmail
servidor.quit()

