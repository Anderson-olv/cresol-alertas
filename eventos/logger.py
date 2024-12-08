import logging  # Biblioteca para geracao de sistema de log rotativo
from logging.handlers import RotatingFileHandler  # Biblioteca utilizada para rotatividade de arquivos de log
from app.variaveis import Globais as vgb  # Importando a classe com as variaveis globais


class LoggerDoApp:
    """ Modulo para carregar o sistema padrao de Logs do app. """
    # Sistema de Logs com logger
    vgb.log = logging.getLogger("Cresol-Alerta")  # Variável capturando os registros de logs e etc
    vgb.log.setLevel(logging.INFO)  # Adicionando o nível do log
    # Formato da linha de log usando data/hota/milisegundos - nivel - numero da linha do programa - mensagem ** %(funcName)s **
    formatter = logging.Formatter('%(asctime)s-%(msecs)03d %(levelname)s: %(message)s ** L%(lineno)d', datefmt='%d/%m/%Y %H:%M:%S')
    loghandler = logging.StreamHandler()  # Adicionando o console do handler
    loghandler = RotatingFileHandler(filename=vgb.caminho_arq_log, mode='a', maxBytes=2000000, backupCount=5)  # Definindo 2 mega por arquivo ate 5 arquivos de bkp
    loghandler.setLevel(logging.INFO)  # Adicionando o nivel do log no handler
    loghandler.setFormatter(formatter)  # Atribuindo o formatter ao handler
    vgb.log.addHandler(loghandler)  # Atribuindo o handler ao logger
    vgb.log_erros_db = logging.getLogger("ERROS")
    vgb.log_erros_db.setLevel(logging.ERROR)
    vgb.log_erros_db.addHandler(loghandler)
