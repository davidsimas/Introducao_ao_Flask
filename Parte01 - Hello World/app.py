# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância da classe Flask, representando a aplicação web
app = Flask(__name__)

# Define um decorador para associar a rota "/" à função index()
@app.route("/")
def index():
    return '<h1>Hello World!</h1>'

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento Flask com modo de depuração ativado
    app.run(debug=True)