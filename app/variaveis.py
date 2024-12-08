import sys
import os


# Variáveis de ambiente
class Globais:
    """ Variaveis Globais do app """
    # VARIAVEIS DINAMICAS
    log: str = None
    
    # DEFININDO A RAIZ DO APP
    raiz_app: str = os.path.abspath(os.getcwd())
    
    # DIRETÓRIO DOS ARQUIVOS COM REGISTROS DE LOGS
    dir_log: str = os.path.join(raiz_app, 'logs')
    temp_status_exec: str = os.path.normpath(os.path.join(dir_log, 'temp_status_exec.txt'))
    caminho_arq_log: str = os.path.normpath(os.path.join(dir_log, 'logs.txt'))  # Arquivo com registro de log atual
    drivers_dir: str = os.path.normpath(os.path.join(raiz_app, 'drivers'))
    
    # Definindo dados padrões para criação de DB, Tabelas e seus valores
    db_site1_portal = "topdesk"
    db_site1_url = "https://cresol.topdesk.net/tas/public/login/form"
    db_site1_usuario = os.getenv("USER")
    db_site1_senha = os.getenv("PASS")