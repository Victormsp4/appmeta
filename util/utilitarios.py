from datetime import datetime, timedelta
from data.database import Dados
from time import sleep

#criando uma base de dados

class Meta:
    def __init__(self,valor,data):
        self.valor = valor
        self.data = data

    @staticmethod
    def data_atual():
        data_atual = datetime.now()
        return data_atual

    #date_database vai receber armazenada no banco de dados 
    @staticmethod
    def data_cronometro(date_database):

        data_atual = datetime.now()
        print(type(data_atual))
        data_alvo = date_database + timedelta(minutes=10)
        while True:
            agora = datetime.now()
            diferença = data_alvo - agora
            if data_alvo < agora:
                break
            print(diferença)
            sleep(1)


base_de_dados = Dados('meusdados')
base_de_dados.create_table('date',Meta.data_atual())
pega_hora_database = base_de_dados.get_valor()
Meta.data_cronometro(pega_hora_database)