# Estrutura de pastas

A seguir, a descrição da estrutura de pastas do projeto

## scrapper

Pasta com os scripts para  realizar o scrapping

## scrapper/data

Pasta com os dados crus coletados

## data

Pasta com os dados consolidados. O arquivo products.json contém a versão final dos dados



## application

Pasta que contém o protótipo de aplicação

# Como usar o scrapper

1. A partir da raiz do projeto, navegar para a pasta scrapper

```shell
cd scrapper
```

2. Utilizar um dos comandos abaixo

```shell
python kabum.py
python pichau.py
python gigantec.py

```

Obs.: Ocasionalmente, Gigantec e Pichau bloqueiam a execução do scrapper. Nesses casos, é necessário rodar o script novamente até que deixem de bloequear (em geral, até duas a três vezes).


# Como rodar o protótipo da aplicação

1. A partir da raiz do projeto, navegar até application/pricetracker

```shell
cd application/pricetracker
```

2. Instalar dependências

```shell
npm install
```

3. Rodar aplicação em modo de desenvolvimento

```shell
npm run dev
```

4. Acessar aplicação em http://localhost:3000