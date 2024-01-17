from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import os
from dotenv import load_dotenv

from smtplib import SMTP 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
    #Variable de entorno
load_dotenv()

def Enviar():

    remitente=os.getenv('USER')
    destinarios= "enderbl1996@gmail.com"
    asunto ='TEST'

    msg= MIMEMultipart()
    msg['Subject']=asunto
    msg['From']= remitente
    msg['To']=destinarios
    #apertura del html con plantilla
    with open('email.html','r') as archivo:
        html =archivo.read()
    #estructura
    msg.attach(MIMEText(html,'html'))
    server= SMTP('mail.clinicaccct.com',587)
    server.starttls()
    server.login(remitente,os.getenv('PASS'))
    server.sendmail(remitente,destinarios,msg.as_string())

def VC():
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
        # time.sleep(20)
        driver.quit()
    except:
        print("Ocurrio un error")


def BNC():
    driver = webdriver.Edge()
    driver.get("https://personas.bncenlinea.com/Auth/LoginJP")
    log=driver.find_element(By.NAME,'CardNumber')
    log.send_keys( os.getenv('BNC_U'))
    boton = driver.find_element(By.ID, "BtnSend")
    boton.click()

BNC()
# <input autocomplete="off" class="form-control ea-triggers-bound" 
# data-val="true" data-val-assertthat="El Número de Tarjeta es inválida, debe ser numérica y tener 16 dígitos." 
# data-val-assertthat-expression="&quot;prv_InnerLoginType == 2 ? IsRegexMatch(CardNumber,'^(62760980)\\\\d{8}$') : IsRegexMatch(CardNumber, '^(619101|619102|619103)\\\\d{10}$')&quot;" 
# data-val-assertthat-fieldsmap="{&quot;prv_InnerLoginType&quot;:&quot;number&quot;,&quot;CardNumber&quot;:&quot;string&quot;}" 
# data-val-assertthat-methodslist="[&quot;IsRegexMatch&quot;]"
#  data-val-required="El Número de Tarjeta es Obligatorio" id="CardNumber" maxlength="16" 
# name="CardNumber" placeholder="Acceso BNCNET" type="tel" value="">

# <button type="submit" class="btn btn-block btn-sm btn-primary transition-3d-hover" id="BtnSend"><i class="fa fa-spinner fa-spin d-none" id="BtnSend_Spiner" style="display:none;"></i><span> Continuar</span></button>

# <i class="fa fa-spinner fa-spin d-none" id="BtnSend_Spiner" style="display:none;"></i>