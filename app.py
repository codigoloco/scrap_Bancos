from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el driver de Chrome
driver = webdriver.Chrome()
driver.get("https://vol.venezolano.com/VOL-Web/login.action")
log=driver.find_element(By.NAME, "datoLogin")
log.send_keys("enderbl1002")
pas=driver.find_element(By.NAME, "claveEntrada")
pas.send_keys("Goku-1996")
boton = driver.find_element(By.ID, "aceptar")
boton.click()
driver.execute_script("GoIB('/VOL-Web/vol/estadoCuenta.do','consultarEstadoCuenta','047')")
driver.execute_script("OpenPDF('000410101998','Corriente')")
time.sleep(160)
driver.quit()

