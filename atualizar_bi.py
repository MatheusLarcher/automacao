from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

# Specify the absolute path to your profile directory
absolute_path_to_profile = "/absolute/path/to/userData"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--headless")
chrome_options.add_argument(f"user-data-dir={absolute_path_to_profile}")  # Use the absolute path
chrome_options.add_argument("profile-directory=Profile 1")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def atualizar_bi_empresa(workspace, empresa):

    driver.get(f"https://app.powerbi.com/groups/{workspace}/list?experience=power-bi")

    seletor = "#content > tri-shell > tri-item-renderer > tri-extension-page-outlet > div:nth-child(2) > workspace-view > tri-workspace-view > tri-workspace-action-base > div > tri-list-filter > div > tri-search-box > input[type=text]"
    digitar_valor_textbox(seletor, empresa)
    
    # Seletor CSS do elemento alvo pra passar o mouse
    seletor = "[data-testid='item-name']"
    
    passar_mouse_sobre_segundo_campo(seletor)
    #       PAROU AQUI              ##############
    print('ok')

def clicar_botao(selector, timeout = 10):
    button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    button.click()


def passar_mouse_elemento(seletor):
    elemento_para_hover = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
    )
    action = ActionChains(driver)
    action.move_to_element(elemento_para_hover).perform()
    

def passar_mouse_sobre_segundo_campo(seletor):
    elementos = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
    )    
    if len(elementos) >= 2:
        elemento_para_hover = elementos[1]
        action = ActionChains(driver)
        action.move_to_element(elemento_para_hover).perform()
    else:
        print("Menos de dois elementos encontrados.")
        
        
def digitar_valor_textbox(selector, texto_entrada, timeout = 10):
    textbox = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    textbox.send_keys(texto_entrada)

if __name__ == "__main__":
    atualizar_bi_empresa('me', '27 de setembro - Plataforma 2D')


