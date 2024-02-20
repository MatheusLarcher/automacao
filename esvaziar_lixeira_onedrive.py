from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def esvaziar_lixeira():
    # Specify the absolute path to your profile directory
    absolute_path_to_profile = "/absolute/path/to/userData"

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-data-dir={absolute_path_to_profile}")  # Use the absolute path
    chrome_options.add_argument("profile-directory=Profile 1")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://2dconsultorescombr-my.sharepoint.com/personal/jean_2dconsultores_com_br/_layouts/15/onedrive.aspx?view=1")

    selector = "#spartan-left-nav > div.navLowerContainer_4c106af6 > div:nth-child(2) > ul > li:nth-child(5) > div"
    clicar_botao(driver, selector, 300)
    
    if(verificar_lixeira_vazia(driver)):
        return
    
    selector = "#appRoot > div > div.body_c231eeb7.ready_c231eeb7 > div > div > div.core_c231eeb7 > div.topBar_c231eeb7 > div > div > div > div > div > div > div > div > div > div > div > div.ms-OverflowSet.ms-CommandBar-primaryCommand.primarySet-62 > div > button > span"
    clicar_botao(driver, selector, 100)
    
    selector = "#appRoot > div > div:nth-child(3) > div.od-OverlayHost > div > div > div.od-Dialog.od-Dialog--close > div.od-Dialog-main.od-Dialog-main--sm.od-Dialog-main-style--normal.od-Dialog-main--allowPanel.od-Dialog-main--dialog.od-Dialog-main--visible > div > div > div.od-Dialog-inner > div.od-Dialog-actions > div > button:nth-child(1)"
    clicar_botao(driver, selector)
    
    selector = "#appRoot > div > div.body_c231eeb7.ready_c231eeb7 > div > div > div.core_c231eeb7 > div.view_c231eeb7 > main > div > div > div > div > div.StandaloneList-content.is-active > div > div.EmptyFolder > div:nth-child(2) > div.EmptyFolder-title"
    clicar_botao(driver, selector, 300)
    
    print("sucesso.")

def clicar_botao(driver, selector, timeout = 10):
    button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    button.click()

def verificar_lixeira_vazia(driver):
    time.sleep(2)
    selector = "#appRoot > div > div.body_c231eeb7.ready_c231eeb7 > div > div > div.core_c231eeb7 > div.view_c231eeb7 > main > div > div > div > div > div.StandaloneList-content.is-active > div > div.EmptyFolder > div:nth-child(2) > div.EmptyFolder-title"
    elements = driver.find_elements(By.CSS_SELECTOR, selector)
    
    if len(elements) > 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    esvaziar_lixeira()


