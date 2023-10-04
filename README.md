# Projeto - Extração de Dados I

<summary><h2>Contexto</h3></summary>

Contexto:
O grupo trabalha no time de engenharia de dados na HealthGen, uma empresa especializada em genômica e pesquisa de medicina personalizada. A genômica é o estudo do conjunto completo de genes de um organismo, desempenha um papel fundamental na medicina personalizada e na pesquisa biomédica. Permite a análise do DNA para identificar variantes genéticas e mutações associadas a doenças e facilita a personalização de tratamentos com base nas características genéticas individuais dos pacientes.

A empresa precisa se manter atualizada sobre os avanços mais recentes na genômica, identificar oportunidades para pesquisa e desenvolvimento de tratamentos personalizados e acompanhar as tendências em genômica que podem influenciar estratégias de pesquisa e desenvolvimento. Pensando nisso, o time de dados apresentou uma proposta de desenvolvimento de um sistema que coleta, analisa e apresenta as últimas notícias relacionadas à genômica e à medicina personalizada, e também estuda o avanço do campo nos últimos anos.


<summary><h2>Criando váriaveis de ambiente - ENV</h3></summary>

Usar arquivos .env em Python é uma prática comum para armazenar informações sensíveis ou configurações que não devem ser codificadas diretamente em seu código fonte. Nesse projeto estamos usando biblioteca python-dotenv para carregar variáveis de ambiente de um arquivo .env.

```bash
API_KEY= SUA_CHAVE_DE_API_AQUI

```

<summary><h2>Execução com Ambiente Virtual</h2></summary>

<details>
<summary><h3>Linux</h3></summary>

## Instale o virtualenv

Para instalar o `virtualenv`, abra o terminal e execute o seguinte comando:

```bash
pip install virtualenv
```

## Criação e Ativação de um Ambiente Virtual

Abra o terminal e navegue até o diretório raiz do projeto, lá crie o ambiente com o seguinte comando:

```bash
virtualenv venv
```

Agora ative seu ambiente virtual:

```bash
source venv/bin/activate
```

## Instlação das ferraments necessárias:

Agora você pode, ainda na pasta raiz, instalar as ferramentas necessárias para rodar a aplicação usando o arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Desativação do ambiente virtual:

Para desativar seu ambiente virtual, basta executar o seguinte comando:

```bash
deactivate
```

</details>

<details>
<summary><h3>Windows</h3></summary>

## Instale o virtualenv

Para instalar o `virtualenv`, abra o Prompt de Comando ou PowerShell como administrador e execute o seguinte comando:

```bash
pip install virtualenv
```

## Criação e Ativação de um Ambiente Virtual

Abra o Prompt de Comando ou PowerShell e navegue até o diretório raiz do projeto, lá crie o ambiente com o seguinte comando:

```bash
virtualenv venv
```

Agora ative seu ambiente virtual:

```bash
venv/bin/activate
```

## Instlação das ferraments necessárias:

Agora você pode, ainda na pasta raiz, instalar as ferramentas necessárias para rodar a aplicação usando o arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Desativação do ambiente virtual:

Para desativar seu ambiente virtual, basta executar o seguinte comando:

```bash
deactivate


