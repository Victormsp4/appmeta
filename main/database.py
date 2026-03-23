import sqlite3

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
        cursor.close()
        return getdado
    
    def apagatd(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_name}")
        conn.commit()
        cursor.close()
