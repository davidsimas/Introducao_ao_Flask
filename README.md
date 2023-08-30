# Aplicação de Comentários com Flask

Esta é uma aplicação web simples desenvolvida com Flask que permite aos usuários enviar comentários
e visualizá-los em uma página da web. A aplicação utiliza o Flask para construir a interface web e
o SQLAlchemy para interagir com o banco de dados.

## Recursos

- Os usuários podem enviar comentários através de um formulário.
- Os comentários enviados são armazenados em um banco de dados SQLite.
- Os comentários podem ser visualizados na página principal.

## Instalação

1. Clone o repositório para sua máquina local:

   git clone https://github.com/davidsimas/Introducao_ao_Flask.git

2. Navegue até o diretório do projeto:

    cd <sua_aplicacao>

3. Crie e ative um ambiente virtual:

    python3 -m venv venv 
    venv\Scripts\activate => no Windows

4. Instale as dependências necessárias:

    pip install -r requirements.txt

5. Execute a aplicação:

    python app.py

6. Acesse a aplicação em seu navegador web em http://localhost:5000.

## Uso

- Acesse a página principal em http://localhost:5000 para visualizar os comentários enviados.
- Utilize o link "Assinar Livro de Visitas" para enviar novos comentários.
- Seus comentários serão armazenados no banco de dados SQLite e exibidos na página principal.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie um novo branch para sua funcionalidade ou correção de bug.
3. Faça suas alterações e faça commits.
4. Envie suas alterações para o fork.
5. Abra um pull request no GitHub com uma descrição detalhada das suas mudanças.
6. Todas as contribuições devem ser submetidas por meio de mensagens do próprio GitHub.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.