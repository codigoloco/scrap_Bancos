from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import selenium
import bd
import time
import os
from env import envio

options = Options()
options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)
options.add_argument("--disable-gpu")  # Desactivar aceleración de GPU

    #Variable de entorno

def BNC():
    var=bd.buscar_Banco("BNC")
    print(var)
    options.add_experimental_option("prefs", {"download.default_directory": r"C:\AdjuntosQSL\BNC"})
    driver = webdriver.Edge( options=options)
    driver.get("https://personas.bncenlinea.com/Auth/LoginJP")
    #ingreso
    log=driver.find_element(By.NAME,'CardNumber')
    log.send_keys(var[4])
    log.send_keys(u'\ue007')
    time.sleep(1)
    log=driver.find_element(By.ID,'UserPassword')
    log.send_keys(var[5])
    log.send_keys(u'\ue007')
    #extraer data del dia anterior
    #redireccion pagina de movimientos previos
    time.sleep(1)
    driver.get('https://personas.bncenlinea.com/Accounts/Transactions/Previous_Day')
    #select de cuenta 
    # try :
    select_element = driver.find_element(By.NAME, 'Account')
    select_object = Select(select_element)
    select_object.select_by_index(1)
    #envio de data selecionada

    time.sleep(1)
    driver.execute_script('document.querySelector("#PnlFilter > div.card.container-card.rounded > div.card-body > div > div.col-12.offset-md-0.col-md-4.pb-md-2 > button").click()')
    time.sleep(3)
    driver.execute_script('document.querySelector("#waitTable > div.row.pt-2 > div > button:nth-child(2)").click()')
    time.sleep(4)
    driver.execute_script('document.querySelector("#Mdl-Information-BtnClose").click()')
    time.sleep(15)

    #agregar click en boton de salir
    driver.execute_script('document.querySelector("#btn-logout").click()')
    time.sleep(1)
    driver.execute_script('document.querySelector("#Mdl-Confirm-Yes").click()')
    #cerrarNAV
    driver.quit()
    envio("BNC")
    # except : 
    #     print("error :  espere 5 minutos antes de volver a ejecutrar 'ya hay una sesion abierta'")

def BVC():

    # Inicializar el driver
    options.add_experimental_option("prefs", {"download.default_directory": r"C:\AdjuntosQSL\BVC"})
    driver = webdriver.Edge(options=options)
    driver.get("https://vob.venezolano.com/")  # Reemplaza con tu URL

    # Esperar a que el iframe esté disponible y cambiar a él
    wait = WebDriverWait(driver, 10)
    iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)

    # Ahora estás dentro del iframe, puedes interactuar con los elementos
    elemento = driver.find_element(By.ID, "login")
    elemento.send_keys(VC_U)
    elemento= driver.find_element(By.ID,"clave")
    elemento.send_keys(VC_P)
    btn=driver.find_element(By.ID,"btnAceptar")
    btn.click()
    #para ingresar a la vista consolidada
    driver.execute_script("enviar('consultarCuentas.do','008');")
    btn= driver.find_element(By.ID,"accountNumber")
    btn.click()
    #javascript:verMovimientosHist();
    driver.execute_script("javascript:verMovimientosHist()")
    #guardar();
    driver.execute_script("guardar()")
    #archivoFile (SE AGREGA EL NOMBRE AL ARCHIVO)
    wait.until(EC.presence_of_element_located((By.ID, "archivoFile")))
    log= driver.find_element(By.ID,"archivoFile")
    #espera
    #colocar el nombre
    time.sleep(3)
    log.send_keys("NOMBRE ARCHIVO")
    #<input name="archivoExt" type="radio" class="radio-vob" value="xls">- document.querySelector("#dialogoArchivo > div.modal-save-radio > div > div:nth-child(4) > input")
    driver.execute_script('document.querySelector("#dialogoArchivo > div.modal-save-radio > div > div:nth-child(4) > input").click()')
    #<input type="button" value="Aceptar" class="button-vob modal-button" onclick="validarDialogoArchivo();">
    driver.execute_script('validarDialogoArchivo();')
    #enviar('logout.do','002');
    driver.execute_script("enviar('logout.do','002');")
    # Regresar al contexto por defecto
    driver.switch_to.default_content()
    # Cerrar el navegador
    driver.quit()
    envio("BVC")



BVC()

