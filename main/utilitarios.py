from datetime import datetime, timedelta
from time import sleep


class Meta:
    def __init__(self,valor,data):
        self.valor = valor
        self.data = data

    @staticmethod
    def data_atual():
        data_atual = datetime.now()
        return data_atual

    #date_database vai receber data armazenada no banco de dados 
    def data_cronometro(self,date_database):
        #o sqlite retorna data dentro de uma tupla que esta dentro de uma lista, no tipo str
        data_string = date_database[0][0]
        #convertendo e especificando ano, med, dia, hora, minuto, segundo e microsegundos.
        convert_data = datetime.strptime(data_string, "%Y-%m-%d %H:%M:%S.%f")
        data_alvo = convert_data + timedelta(minutes=5)
        while True:
            agora = datetime.now()
            diferença = data_alvo - agora
            if data_alvo < agora:
                break
            print(diferença)
            sleep(1)
