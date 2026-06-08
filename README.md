# Global Solution Computational Thinking with Python

Este repositório contém o código-fonte Computational Thinking with Python do projeto desenvolvido para a Global Solution. 

## Sumário

- [Objetivo](#objetivo)
- [Tecnologia Utilizada](#tecnologia-utilizada)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Funcionalidades](#funcionalidades)
- [Execução do Projeto](#execução-do-projeto)
- [Integrantes](#integrantes)

## Objetivo



## Tecnologia Utilizada

- Python
- Python Dotenv
- OpenWeather API

## Estrutura de Arquivos

A arquitetura do projeto está organizada da seguinte maneira:

```text
/global-solution-computational-thinking
  ├── /config
  │      └── config.py
  ├── /services
  │       ├── clima.py
  │       └── limpeza.py   
  ├── /ui
  │    └── menu.py
  ├── main.py
  └── README.md
```

## Funcionalidades

- Consultar previsão do tempo de uma cidade.
- Verificar estimativa de chuva para os próximos 5 dias.
- Simular a necessidade de limpeza de painéis solares.
- Executar limpeza automática ou manual.
- Registrar histórico de limpezas realizadas.
- Gerar relatórios de eficiência recuperada.
- Calcular economia estimada de energia e manutenção.

## Execução do Projeto

### Pré-requisitos

Antes de executar o sistema, certifique-se de possuir:

- Python 3.10 ou superior
- Conta na OpenWeather
- Chave de API da OpenWeather

### Instalação das Dependências

Execute o comando abaixo no terminal:

```bash
pip install requests python-dotenv
```

### Configuração da API
Crie um arquivo `.env` na raiz do projeto:

```env
api_key=SUA_CHAVE_AQUI
```

### Executando o Projeto

Na raiz do projeto, execute:

```bash
python main.py
```

### Utilização

Ao iniciar o sistema, será exibido um menu com as seguintes opções:

1. Definir local e obter previsão do tempo.
2. Estimativa de chuva (próximos 5 dias).
3. Simulador de limpeza.
4. Limpar painel solar.
5. Exibir relatório de limpezas.
0. Sair.

Basta selecionar uma das opções e seguir as instruções exibidas no terminal.

## Integrantes

| Integrantes | RM |
| --- | :---: |
| `Diego Rayhan Jalhium Machado` | 569129 |
| `Gabriel Almeida dos Santos` | 573690 |
| `Kaue Tsuyoshi Horoiwa` | 571192 |
| `Roberto Dantas Melo Filho` | 566716 |