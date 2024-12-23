# Projeto: Automação de Chamados com Python

## Descrição

Este projeto tem como objetivo analisar se as analises estão sendo feitas no horário pré-acordado junto ao time.

---

## Funcionalidades Planejadas

1. **Leitura de Planilha Online**:
   - Acessar uma planilha através de um link.
   - Ler informações de linhas e colunas específicas para identificar se um chamado está registrado.

2. **Verificação de Chamados**:
   - Identificar se a célula correspondente ao chamado está vazia ou preenchida.
   - Analisar os detalhes do chamado, se já existente.

3. **Abertura e Análise de Chamados**:
   - Criar novos chamados caso não exista um registrado.
   - Realizar ações automatizadas baseadas nos dados preenchidos.

---

## Tecnologias e Ferramentas

- **Python**: Linguagem de programação principal do projeto.
- **Google Sheets API**: Para integração e leitura da planilha online.
- **Requests ou Bibliotecas de API**: Caso seja necessário acessar APIs para gerenciar chamados.
- **Pandas**: Para manipulação e análise de dados da planilha.
- **Logging**: Para rastrear as atividades e status do sistema.

---

## Estrutura do Projeto

```plaintext
/
├── src/
│   ├── main.py          # Script principal do projeto
│   ├── sheets_reader.py # Funções para leitura e manipulação da planilha
│   ├── chamado_handler.py # Funções para análise e abertura de chamados
│   └── utils.py         # Utilitários e funções auxiliares
├── data/
│   ├── settings.json    # Configurações da API e credenciais
├── logs/
│   └── activity.log     # Registro de logs do sistema
├── README.md            # Documentação do projeto
└── requirements.txt     # Bibliotecas e dependências do Python
```

---

## Diagrama

![Descrição do Fluxograma](/docs/cresol.drawio.png)

---