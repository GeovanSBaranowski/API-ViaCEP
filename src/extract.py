import pandas as pd

#extrai os itens do .csv carregado no projeto, recebendo a variavel direto do .config e convertendo os itens em uma lista
def extract_cep(path):
    df_ceps = pd.read_csv(path, dtype={'cep': str})
    return df_ceps['cep'].to_list()