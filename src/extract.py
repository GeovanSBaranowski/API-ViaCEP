import pandas as pd

def extract_cep(path):
    df_ceps = pd.read_csv(path, dtype={'cep': str})
    return df_ceps['cep'].to_list()