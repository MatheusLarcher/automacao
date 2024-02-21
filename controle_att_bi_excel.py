import pandas as pd
import os
import sys

def atualizar_controle_empresas():
    if getattr(sys, 'frozen', False):
        # O script está sendo executado em um bundle criado pelo PyInstaller
        diretorio_atual = os.path.dirname(sys.executable)
    else:
        # O script está sendo executado normalmente (não é um executável PyInstaller)
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        
    nome_arquivo = "Controle Atualizações.xlsx"
    caminho_completo = os.path.join(diretorio_atual, nome_arquivo)

    if not os.path.exists(caminho_completo):
        df = pd.DataFrame(columns=['Workspace', 'Empresa', 'data_att'])
        df.to_excel(caminho_completo, index=False)
        print('Cadastre as empresa no arquivo: Controle Atualizações.xlsx ')
        sys.exit(0)

    from atualizar_bi import obter_data_att
    
    data_empresas = pd.read_excel(caminho_completo)
    lista_empresas = []

    for indice, empresa in data_empresas.iterrows():
        workspace = empresa['Workspace']
        data_att = obter_data_att(workspace, empresa['Empresa'])
        dados_empresa = {'Workspace': workspace, 'Empresa': empresa['Empresa'], 'data_att': data_att}
        lista_empresas.append(dados_empresa)

    df_empresas = pd.DataFrame(lista_empresas)
    df_empresas.to_excel(caminho_completo, index=False)

# Chama a função para executar o processo
atualizar_controle_empresas()