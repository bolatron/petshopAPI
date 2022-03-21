# Petshop API
Resolução desenvolvida para o desafio enviado pela ZarpSystem.

## 1 - Pacotes necessários:
  * Python >= 3.9.6
  * Django >= 4.0
  
#### 1.1 - Instalação:
  1. Clone o repositório usando: <code>git clone https://github.com/ArthurGM18/petshopAPI</code>.
  2. Utilize <code>cd petshopAPI/</code> para entrar na pasta raiz do projeto.
  3. Utilize <code>docker-compose up --build</code> para instalar todas as dependências.
  4. Rode o comando <code>docker-compose up</code> para subir o container e rodar a API.
 
## 2 - Sobre o Sistema

#### 2.1 - Funcionamento geral

  O sistema desenvolvido administra o CRUD das entidades Tutor e Animal para uma API de petshop utilizando o DRF (Django Rest Framework). Boas práticas REST foram aplicadas para alinhar melhor as expectativas sobre o resultado da API desenvolvida.
  
## 3 - Endpoints

  Exemplos:

  Para criação de um novo Tutor:
  <code> ccurl -X POST 'localhost:8000/api/tutors/' --header 'Content-Type: application/json' --data-raw '{"first_name":"Teste","last_name":"Teste","email":"email@email.com","password":"123","phone":"9999-8888","status":"Acti"}' </code>
  
  Para criação de um novo Animal:
  <code> curl -X POST "localhost:8000/api/animals/" -H "Content-Type: application/json" --data-raw '{"name" : "Tobias", "birth_date": "1999-02-02", "type": "DOG", "breed": "Pastore", "status": "ACTI"}' </code>
  
  Para listar todos os Animais (mesma lógica para Tutor):
  <code> curl -X GET "localhost:8000/api/animals/"
 
  Para listar um animal pelo id (mesma lógica para Tutor):
  <code> curl -X GET "localhost:8000/api/animals/<id:int>/"
   
  Para atualizar algum animal (mesma lógica para Tutor):
  <code> curl -X PATCH 'localhost:8000/api/animals/<id:int>/' --header 'Content-Type: application/json' --data-raw '{"status":"PEND"}' </code>
   
  Para deletar um animal (mesma lógica para Tutor):
  <code> curl -X DELETE 'localhost:8000/api/animals/<id:int>/'
   
 #### 3.1 Exclusão Lógica
   
   Como pedido na documentação, foi adicionado um campo **is_deleted** aos modelos de Tutor e Animal que é utilizada para filtrar todas as instâncias que forem deletadas via API, porém ainda irão existir no banco de dados.
  
