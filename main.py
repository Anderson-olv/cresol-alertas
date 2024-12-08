from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente
import sys  # Biblioteca para interagir com o sistema operacional
import os  # Biblioteca para interagir com o sistema operacional
import time  # Biblioteca para manipular tempo
import urllib3  # Biblioteca para manipular requisições HTTP para desativar verificacao de ssl nao verificado google
import logging  # Usado para desativar o log do webdriver-manager
from selenium import webdriver  # Biblioteca para manipular o navegador
from selenium.webdriver.chrome.service import Service as ChromeService  # Importando o servico webdriver do selenium e definando o nome para o servico no chrome
from selenium.webdriver.chrome.service import Service  # Biblioteca para manipular o serviço do navegador
from selenium.webdriver.common.by import By  # Biblioteca para manipular elementos do navegador
from selenium.webdriver.common.keys import Keys  # Biblioteca para manipular teclas do teclado
from selenium.webdriver.chrome.options import Options  # Biblioteca para manipular opções do navegador
from selenium.webdriver.common.action_chains import ActionChains  # Biblioteca para manipular ações do mouse
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # Biblioteca para manipular capacidades do navegador
from selenium.webdriver.support.ui import WebDriverWait  # Biblioteca para manipular espera do navegador
from selenium.webdriver.support import expected_conditions as EC  # Biblioteca para manipular condições esperadas do navegador
from selenium.common.exceptions import *  # Biblioteca para manipular exceções do navegador
load_dotenv()  # Carrega variáveis do arquivo .env para o ambiente
from app.variaveis import Globais as vgb  # Biblioteca com variáveis globais

if sys.platform.startswith('win32'):  # Valida se o sistema e windows ou linux
    from subprocess import CREATE_NO_WINDOW  # Biblioteca usada para nao abrir janela do prompt ao realizar o download automatico do driver atualizado ao executar o robo

class Main:
    def __init__(self):
        self.fluxo()
        self.driver: webdriver.Chrome = None
        self.vars: dict = {}

    def iniciar(self):
        print('Iniciando...')
        urllib3.disable_warnings()  # Desativando aviso de ssl nao verificado, pois, sao sistemas internos.
        os.environ['WDM_SSL_VERIFY'] = '0'  # Definindo para zero devido a erro de SSL auto assinado, removendo a verificacao
        logging.getLogger('WDM').setLevel(logging.NOTSET)  # Desabilitando o log do wdm webdriver-manager (Pode ser descomentado a qualquer momento)
        os.environ['WDM_LOG'] = '0'  # Desabilitando o log do wdm webdriver-manager (Pode ser descomentado a qualquer momento)
        os.environ['WDM_PRINT_FIRST_LINE'] = 'False'  # Desabilitando a insercao de linhas em branco no log do webdriver-manager
        vgb.log.info('-------------------------CARREGANDO-CHROME-------------------------')  # Mensagem informativa iniciando o carregamento do navegador
        options = webdriver.ChromeOptions()  # Definindo opcoes para o webdriver para o chrome
        options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Desabilitando a captura padrao de bluetooth do navegador
        service = ChromeService(log_path=os.path.join(vgb.drivers_dir, 'chromedriver.log'))  # executable_path=ChromeDriverManager(path=vgb.drivers_dir).install())  # Construindo o servico, download e instalacao do driver automaticamente
        if sys.platform.startswith('win32'):
            service.creation_flags = CREATE_NO_WINDOW  # CREATE_NO_WINDOW desativa a abertura do terminal para download do driver
        self.driver = webdriver.Chrome(options=options, service=service)  # Passando o webdriver para a classe servico e inicializando e realizando o download automatico chrome
        # self.inicio_acesso_cef_controller()  # Chamando funcao
        time.sleep(1)
        
    
    def fechar(self):
        print('Encerrando...')
        time.sleep(1)
        

    def fluxo(self):
        self.iniciar()
        print('Executando Fluxo...')
        self.fechar()
        sys.exit(0)
        
if __name__ == '__main__':
    from app.diretorios import ValidaArquivosDiretorios as vad
    vad.validar()
    from eventos.logger import LoggerDoApp
    Main()
    