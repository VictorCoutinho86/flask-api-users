# -*- coding: utf-8 -*-

from os import getenv
from os.path import dirname, isfile, join

from dotenv import load_dotenv

# Obtém o arquivo com as variáveis de ambiente
_ENV_FILE = join(dirname(__file__), '.env')

# Se o arquivo existe faz a leitura do mesmo com a função load_dotenv
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from apps import create_app

# Instância a Factory criada em apps
app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    ip = '0.0.0.0'
    debug = app.config['DEBUG']
    port = app.config['APP_PORT']

    app.run(host=ip, debug=debug, port=port, use_reloader=debug)
