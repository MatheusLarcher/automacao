import pandas as pd

import streamlit as st




# Criando um cursor para o banco de dados de destino para executar operações
destino_cur = destino_conn.cursor()

try:
    # Lendo dados do banco de dados de origem
    df = pd.read_sql_query('SELECT * FROM tabela_origem', origem_conn)
    
    # Transformação dos dados, se necessário
    # Exemplo: df = df[df['alguma_coluna'] > 0]
    
    # Carregando dados no banco de dados de destino
    for index, row in df.iterrows():
        destino_cur.execute(
            "INSERT INTO tabela_destino (coluna1, coluna2, ...) VALUES (%s, %s, ...)",
            (row['coluna1'], row['coluna2'], ...)
        )
    
    # Commit das inserções
    destino_conn.commit()
    
finally:
    # Fechando conexões
    destino_cur.close()
    destino_conn.close()
    origem_conn.close()

print("ETL realizado com sucesso!")
