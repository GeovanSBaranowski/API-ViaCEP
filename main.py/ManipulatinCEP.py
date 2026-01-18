import requests
import pandas as pd
import os

endereco_retorno = []
endereco_erro = []

cep = pd.read_csv('data/Lista_ceps.csv', dtype={'cep': str})

for ceps in cep['cep']:
    url= f'https://viacep.com.br/ws/{str(ceps).strip()}/json/'


    try:
         response = requests.get(url= url)
         response.raise_for_status()

         retorno = response.json()

         if retorno.get('erro'):
              endereco_erro.append(retorno)
              continue
         
         endereco_retorno.append(retorno)
              

    except:
         print(f'O cep {ceps} é invalido')

endereco_validos = pd.DataFrame(endereco_retorno)
endereco_validos.to_csv('data/enderecos_validos.csv', mode='a', index=False, header= not os.path.exists('data/enderecos_validos.csv'), encoding='utf8')

endereco_invalidos = pd.DataFrame(endereco_erro)
endereco_invalidos.to_csv('data/enderecos_invalidos.csv', mode='a', index=False, header= not os.path.exists('data/enderecos_invalidos.csv'), encoding='utf8')