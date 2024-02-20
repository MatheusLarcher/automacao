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
    
    seletor = "#artifactContentView > div.cdk-virtual-scroll-content-wrapper > div:nth-child(3) > div:nth-child(2) > div > span > button:nth-child(2) > mat-icon"
    clicar_botao(seletor)

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
    elementos = driver.find_elements(By.CSS_SELECTOR, seletor)
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

def obter_valor_textbox(seletor):
    elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
    )
    texto = elemento.text
    return texto

def obter_data_atualizacao(seletor):
    elemento = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
    )
    texto_completo = elemento.text
    prefixo = "Data Atualização: "
    if texto_completo.startswith(prefixo):
        data_atualizacao = texto_completo[len(prefixo):]
        return data_atualizacao
    
def obter_data_att(workspace, empresa):
    driver.get(f"https://app.powerbi.com/groups/{workspace}/list?experience=power-bi")

    seletor = "#content > tri-shell > tri-item-renderer > tri-extension-page-outlet > div:nth-child(2) > workspace-view > tri-workspace-view > tri-workspace-action-base > div > tri-list-filter > div > tri-search-box > input[type=text]"
    digitar_valor_textbox(seletor, empresa)
    
    #abrir bi
    seletor = "[data-testid='item-name']"
    clicar_botao(seletor)
    
    seletor = "#content > tri-shell > tri-item-renderer > tri-extension-page-outlet > div:nth-child(2) > report > exploration-container > div > div > docking-container > div > div > exploration-fluent-navigation > section > nav > mat-action-list > button.mat-list-item.mat-focus-indicator.exploration-fluent-li.item.trimmedTextWithEllipsis.fluentTheme-sm-reg.selected.ng-star-inserted"
    clicar_botao(seletor)
    
    seletor = "text.value"
    valor = obter_data_atualizacao(seletor)
    
    
    print(valor)

if __name__ == "__main__":
    obter_data_att('me', 'Columbia - Plataforma 2D')
    driver.close()


##7 Lagoas - Plataforma 2D
#Altese - Plataforma 2D
