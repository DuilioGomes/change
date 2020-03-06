# Change

Este projeto contem uma url para calcular e fornecer o troco com a menor quantidade de notas.
Além de conter um CRUD de transação que utiliza da mesma funcionalidade para fornecer o melhor troco.

## Requisitos

- Python 3.7+
- Pip pachage manager
- Mongo

## Instalação

> A documentação segue uma instalação baseada em ambiente Linux Ubuntu 19.10

Após realizar o clone do projeto, certifique-se que o banco de dados MongoDB esta instalado e rodando

- Acesse o banco de dados Mongo, e crie um banco com o nome 'change', com os comandos:
```bash
mongo
use change
``` 

- instale os requisitos python, utilizando o comando:
```bash
pip install -r requirements.txt
```

## Inicialização do projeto

Para inicializar o servidor, entre na pasta que contém o arquivo 'manage.py' e utilize o seguintes comandos:

```bash
./manage.py migrate
./manage.py runserver
```

O primeiro comando atualizará o banco de dados e o segundo é responsável por inicializar o servidor

Por padrão, o servidor utiliza a porta 8000 do localhost, podendo ser acessada através dos endereços:

> http://127.0.0.1:8000/

> http://localhost:8000/


## Utilização

**Opcional**

> Dentro do projeto existe um arquivo chamado 'change_postman.json', 
que pode ser importado dentro do aplicativo postman.
O arquivo contém uma collection das requisições que podem ser feitas para o servidor.


Exitem 2 principais urls, a primeira que realiza apenas o calculo de troco pode ser acessada:

> http://127.0.0.1:8000/cashier/simple_cashier

Ela espera uma chamada do tipo POST, onde seu body deve conter um json seguindo o formato abaixo

```javascript
{
    "amount_paid": 100.00,
    "amount_charged": 23.23
}
```

A segunda url, consiste do CRUD da transação.
 
 Está url aceita os metodos GET, PUT, POST e DELETE.
 Ela pode ser acessada utilizando o caminho:
 
> http://127.0.0.1:8000/cashier/transaction

O formatado do dado enviado se mantem igual:

```javascript
{
    "amount_paid": 140.00,
    "amount_charged": 43.43
}
```

Os metodos GET pode receber um parametro **id** para retornar apenas uma transação com detalhes.

E os metodos PUT e DELETE necessariamente precisam desse mesmo parametro para alterar e excluir o documento desejado.
Esse parametro deve ser passado como no exemplo abaixo, onde o 1 é o **id**

> http://127.0.0.1:8000/cashier/transaction/1




## Autor
- Duilio Carvalho Gomes
