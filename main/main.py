from database import Dados
from utilitarios import Meta

base_de_dados = Dados('mydata.db')
minha_meta = Meta(500,5)
data_atual = Meta.data_atual()
base_de_dados.create_table('data', data_atual)
pega_hora_database = base_de_dados.get_valor()


minha_meta.data_cronometro(base_de_dados.get_valor())