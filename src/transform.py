import re
import requests
import json

def cep_valido(cep): #funcao para validar se o cep esta dentro do padrao
    return bool(re.fullmatch(r'\d{8}', cep)) #e feito um fullmatch son o cep, usar raw string para valida integralmente a string, passando o parametro de 8 digitos

def transforma_cep(cep, base_url):
    if not cep_valido(cep): #chama a funcao cep_valido para validar o item atual
        return None #caso seja invalido, nao retorna nada
    

    url = f'{base_url}/{cep}/json/' #Monta a URL para a API

    response = requests.get(url) #faz a requisicao na API

    if response.status_code != 200: #se o retono nao for sucessso, ignora
        return None
    
    data = response.json() #armazena a resposta 

    if data.get('erro'): #caso a resposta seja erro, ignora
        return None
    
    #retorna o conjunto de dados caso passe pelas validacoes
    return  {
        'CEP': data['cep'],
        'Logradouro': data['logradouro'],
        'Bairro': data['bairro'],
        'Cidade': data['localidade'],
        'Estado': data['uf']
    }



