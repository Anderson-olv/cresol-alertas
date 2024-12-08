import logging  # Biblioteca para geração de sistemas de log
from logging.handlers import RotatingFileHandler  # Biblioteca para geração de sistemas de log rotativos
from app.variaveis import Globais  as vgb  # Importa as variáveis globais


class LoggerDoApp:
    """ Modulo para gerar logs do sistema """
    # Configuração do logger
    vgb.log = logging.getLogger('app')
    vgb.log.setLevel(logging.INFO)  # Adiciona o nível de log
    # Formato da linha de log usando data/hora/milissegundos/nível de log/nome do módulo/mensagem
    formatter = logging.Formatter('%(asctime)s-%(msecs)03d %(levelname)s: %(message)s ** L%(lineno)d', datefmt='%d/%m/%Y %H:%M:%S')
    loghandler = logging.StreamHandler()  # Adicionando o console do handler
    loghandler = RotatingFileHandler(filename=vgb.caminho_arq_log, mode='a', maxBytes=2000000, backupCount=5)  # Definindo 2 mega por arquivo ate 5 arquivos de bkp
    loghandler.setLevel(logging.INFO)  # Adicionando o nível do log no handler
    loghandler.setFormatter(formatter)  # Atribuindo o formatter ao handler
    vgb.log.addHandler(loghandler)  # Atribuindo o handler ao logger
    vgb.log_erros_db = logging.getLogger("ERROS")
    vgb.log_erros_db.setLevel(logging.ERROR)
    vgb.log_erros_db.addHandler(loghandler)
    