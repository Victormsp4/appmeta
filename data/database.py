from util.utilitarios import *
import sqlite3
from datetime import datetime

class Dados:
    def __init__(self, name_database):
        self.name_database = name_database

    #metodo interno
    def _connect(self):
        return sqlite3.connect(self.name_database)
    
    def create_table(self,table_name,valor):
        self.table_name = table_name
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}(valor INTEGER)")
        cursor.execute(f"INSERT INTO {self.table_name} VALUES(?)", (valor,))
        conn.commit()
        cursor.close()
    
    def get_valor(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        getdado = cursor.fetchall()
        print(type(getdado))
        conn.commit()
        cursor.close()

dataagora = Meta.data_atual()
hora = datetime.now()
d1 = Dados('meusdados.db')
d1.create_table('teste',dataagora)
d1.get_valor()
