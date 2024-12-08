import os
from app.variaveis import Globais as vgb  # Importando a classe com as variáveis globais


class ValidaArquivosDiretorios:
    """ Modulo utilizado para validação e identificação de arquivos e diretórios padrões do app. """

    @classmethod
    def validar(cls) -> None:
        os.makedirs(vgb.drivers_dir, exist_ok=True)
        os.makedirs(vgb.dir_log, exist_ok=True)
        if not os.path.isfile(vgb.caminho_arq_log):
            with open(vgb.caminho_arq_log, mode='a') as f:
                pass