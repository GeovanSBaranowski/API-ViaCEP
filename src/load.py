import pandas as pd
import os

#funcao recebendo data = lista onde foi armazena o resultado da requisicao
#e path = diretorio onde sera criado o csv
def load_ceps(data, path): 
    
    if not data: #se nao receber nada, ignora
     return None
    
    #Verifica se ja existe ou nao o diretorio, se nao existir, cria um
    #se existir, armazena no mesmo
    os.makedirs(os.path.dirname(path), exist_ok= True)

    #cria o dataframe com as informacoes retornadas da pipeline e o transforma em um .csv
    df_ceps = pd.DataFrame(data)
    df_ceps.to_csv(path, index=False, encoding='utf-8')