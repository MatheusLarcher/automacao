import psycopg2

def get_database_connection(dbname, user, password, host, port):
    
    conexao_bd = f"dbname={dbname} user={user} password={password} host={host} port={port}"
    conn = psycopg2.connect(conexao_bd)
    cursor = conn.cursor()
    return cursor


import fdb

dsn = '192.168.6.250:/home/emsoft_bd/altese_galpao.fdb'
user = 'sysdba'
password = 'masterkey'


def get_database_connection(dsn, user, password):
    con = fdb.connect(dsn=dsn, user=user, password=password)
    cursor = con.cursor()
    return  cursor

conexao = get_database_connection(dsn, user, password)

tb = conexao.execute("SELECT * FROM est")
print(tb)

