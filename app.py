from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib
from email.mime.text import MimeText

# Datos del remitente
remitente = "enderbl1996@gmail.com"
contraseña_remitente = "Goku-1996"

# Datos del destinatario
destinatario = "e.blanco@clinicaccct.com"

# Crear el objeto MimeText con el contenido del correo
mensaje = MimeText("Este es un correo electrónico enviado desde Python")

# Establecer los encabezados del correo
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = "Envío de correo electrónico desde Python"

# Enviar el correo
server = smtplib.SMTP("mail.gmail.com", 587)
server.login(remitente, contraseña_remitente)
server.send_message(mensaje)
server.quit()

def Descarga():
    try :
        driver = webdriver.Edge()
        driver.get("https://vol.venezolano.com/VOL-Web/login.action")
        log=driver.find_element(By.NAME, "datoLogin")
        log.send_keys("enderbl1002")
        pas=driver.find_element(By.NAME, "claveEntrada")
        pas.send_keys("Goku-1996")
        boton = driver.find_element(By.ID, "aceptar")
        boton.click()
        driver.execute_script("GoIB('/VOL-Web/vol/estadoCuenta.do','consultarEstadoCuenta','047')")
        driver.execute_script("OpenPDF('000410101998','Corriente')")
        driver.execute_script("salir()")
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(60)
        driver.quit()
    except:
        print("Ocurrio un error")

