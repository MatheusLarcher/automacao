from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass
from selenium.common.exceptions import TimeoutException

def verificar_tela_login(driver):
    time.sleep(2)
    # Verifica se o campo de entrada de usuário está presente
    selector_usuario = '#i0116'
    elements_usuario = driver.find_elements(By.CSS_SELECTOR, selector_usuario)
    
    # Verifica se o botão de entrar está presente
    selector_entrar = '#i0118'
    elements_entrar = driver.find_elements(By.CSS_SELECTOR, selector_entrar)
    
    return len(elements_usuario) > 0 and len(elements_entrar) > 0

def esvaziar_lixeira(headless = False):
    # Caminho onde será salvo os caches do navegador
    usuario = getpass.getuser()
    absolute_path_to_profile = f"C:\\Users\\{usuario}\\AppData\\Local\\Google\\Chrome\\User Data"

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    if (headless):
        chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-data-dir={absolute_path_to_profile}")
    chrome_options.add_argument("profile-directory=Profile 1")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://2dconsultorescombr-my.sharepoint.com/personal/jean_2dconsultores_com_br/_layouts/15/onedrive.aspx?view=5")

    
    if(verificar_lixeira_vazia(driver, 2)):
        return
    
    
    #botao Esvaziar lixeira
    selector = 'button[aria-label="Esvaziar lixeira"]'
    clicar_botao(driver, selector, 10)
    
    #botao confirmar
    #selector = "#appRoot > div > div:nth-child(3) > div.od-OverlayHost > div > div > div.od-Dialog.od-Dialog--close > div.od-Dialog-main.od-Dialog-main--sm.od-Dialog-main-style--normal.od-Dialog-main--allowPanel.od-Dialog-main--dialog.od-Dialog-main--visible > div > div > div.od-Dialog-inner > div.od-Dialog-actions > div > button:nth-child(1)"
    #clicar_botao(driver, selector)

    clicar_botao_descricao(driver, "Sim")
    
    if(verificar_lixeira_vazia(driver, 90)):
        driver.close()
    
    print("sucesso.")

def clicar_botao(driver, selector, timeout = 10):
    button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    button.click()

def clicar_botao_descricao(driver, descricao_botao, timeout=10):
    try:
        # Procura o botão pelo texto do label que é "Sim".
        botao_confirmar = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[.//span[contains(text(), '{descricao_botao}')]]")))
        botao_confirmar.click()
        return True
    except TimeoutException:
        return False
    
def verificar_lixeira_vazia(driver, timeout=10):
    selector = "#appRoot > div > div.body_68bb4b5e.ready_68bb4b5e > div > div > div.core_68bb4b5e > div.view_68bb4b5e > main > div > div > div > div > div.StandaloneList-content.is-active > div > div.EmptyFolder > div:nth-child(1)"
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        return True
    except TimeoutException:
        return False
    
if __name__ == "__main__":
    esvaziar_lixeira()
