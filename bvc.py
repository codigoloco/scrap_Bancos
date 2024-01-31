import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


VC_U='JGQUINTERO'
VC_P='Qscom28.'
# Inicializar el driver
driver = webdriver.Edge()
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