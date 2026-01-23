from utilities.loader_config import load_config
from extract import extract_cep
from transform import transforma_cep
from load import load_ceps

def run():

     config = load_config()

     #variaveis com os valores do config.yaml
     base_url = config['API']['BASE_URL']
     input_path = config['DATA']['INPUT_DATA']
     output_valid = config['DATA']['OUTPUT_DATA_VALID']
     output_invalid = config['DATA']['OUTPUT_DATA_INVALID']

     #chama a funcao de extracao, vinda do arquivo csv carregado no projeto e armazena na variavel
     df_ceps = extract_cep(input_path)
   
     #listas de armazenamento de retornos da fase de transformacao
     endereco_ok = []
     endereco_erro = []

     #percorre os itens extraidos na variavel ceps e os separa
     for cep in df_ceps:
          resultado_cep = transforma_cep(cep, base_url)

     #caso o resultado seja 200 e possua valor diferente de 'erro' o item é armazenado na lista 'endereco_ok'
     #caso o retorno da funcao 'retorna_cep' seja diferente de 200 ou valor igual a 'erro' é armazenado na lista 'endereco_erro'
          if resultado_cep: 
               endereco_ok.append(resultado_cep)
          else:
               endereco_erro.append({'cep': cep})

     load_ceps(endereco_ok, output_valid) #cria o .csv com enderecos validos
     load_ceps(endereco_erro, output_invalid) #cria o .csv com enderecos invalidos

#chama a funcao run apenas quando executada a partir deste arquivo
if __name__ == "__main__":
     run()