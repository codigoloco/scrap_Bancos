import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from bd import LEER ,buscar_Banco,Error,enviado
import os
from datetime import datetime,timedelta

def B_archivos(var):
    ruta=f'C:\AdjuntosQSL\{var}'

    lista= os.listdir(ruta)
    lista = [arch for arch in lista if os.path.isfile(os.path.join(ruta, arch))]
    if var== "BNC":
        lista =f'C:\AdjuntosQSL\{var}\{lista[0]}'

    return lista


def envio(banco):
    res= LEER()
    archivo = B_archivos(banco) # El nombre del archivo que quieres adjuntar
    banco =buscar_Banco(banco)
    fec= datetime.now()
    fec= fec- timedelta(days=1)
    form= "%Y%m%d"
    print(form)
    fec_for=fec.strftime(form)
    print(fec_for)
    #Variables del correo
    # asunto rif cuenta fechaInvertida 
    subject = f"{banco[1]} {banco[2]} {fec_for}"
    body = f' Se adjunta estado de cuenta bancario correspondiente a {banco[1]} {banco[2]} \n '
    # datos de bd
    sender = res[0]
    recipients = ["e.blanco@clinicaccct.com","qslservicio@gmail.com"]
    password = res[1]
    port=res[2]
    host=res[3] 

    # --variables
    # sender = "e.blanco@clinicaccct.com"
    # recipients = ["enderbl1996@gmail.com"]
    # password = "Clinica181014"
    # port=465
    # host="mail.clinicaccct.com"

    #variables2
    # sender = "testmovimientosqsl@gmail.com"
    # recipients = ["e.blanco@clinicaccct.com"]
    # password = "utsf rynk rkbv bxku"
    # port=465
    # host="smtp.gmail.com"

    def send_email(subject, body, sender, recipients, password, archivo):
        # Creamos el objeto MIMEMultipart
        msg = MIMEMultipart()
        # Asignamos los atributos del correo electrónico
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        # Adjuntamos el cuerpo del mensaje como una parte MIMEText
        msg.attach(MIMEText(body, 'plain'))
        # Abrimos el archivo que queremos adjuntar en modo binario
        with open(archivo, "rb") as f:
            # Creamos el objeto MIMEBase
            part = MIMEBase('application', 'octet-stream')
            # Leemos el contenido del archivo
            part.set_payload(f.read())
            # Codificamos el contenido en base64
            encoders.encode_base64(part)
            # Añadimos el encabezado con el nombre del archivo
            part.add_header('Content-Disposition', "attachment; filename= %s" % archivo)
            # Adjuntamos el archivo como una parte MIMEBase
            msg.attach(part)
        # Creamos una conexión al servidor SMTP
        servidor = host # La dirección del servidor SMTP
        puerto = port # El puerto del servidor SMTP
        usuario = sender # El usuario del correo electrónico
        contraseña = password # La contraseña del correo electrónico
        try:
            sesion_smtp = smtplib.SMTP_SSL(servidor, puerto)
            # Iniciamos sesión en el servidor SMTP
            sesion_smtp.login(usuario, contraseña)
            # Convertimos el objeto MIMEMultipart a texto
            texto = msg.as_string()
            # Enviamos el correo electrónico
            sesion_smtp.sendmail(sender, recipients, texto)
            # Cerramos la conexión al servidor SMTP
            sesion_smtp.quit()
            desc=f'{banco[3]}+{banco[1]}'
            enviado(desc,"enviado",datetime.now())
        except Exception as E:
            Error(E)

    send_email(subject, body, sender, recipients, password, archivo)
    
envio("BVC")