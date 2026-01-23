import yaml

#transforma o .config em uma funcao, permitindo-se usa-la em outros modulos de maneira maiss facilitada
def load_config():
    with open('config/config.yaml', 'r', encoding='utf-8') as conf:
        return yaml.safe_load(conf)
