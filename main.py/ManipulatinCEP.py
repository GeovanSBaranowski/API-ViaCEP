import requests
import pandas as pd

cep = pd.read_csv('data/Lista_ceps.csv', dtype={'cep': str})

for ceps in cep['cep']:
    url= f'https://viacep.com.br/ws/{str(ceps).strip()}/json/'

    

    try:
         response = requests.get(url= url)
         response.raise_for_status()
         
         print(response.json())

    except:
         print(response)