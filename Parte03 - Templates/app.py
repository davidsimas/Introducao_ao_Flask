# Importa a classe Flask do módulo flask
from flask import Flask, render_template

# Cria uma instância da classe Flask, representando a aplicação web
app = Flask(__name__)

# Define um decorador para associar a rota "/" à função index()
@app.route("/")
def index():
    return '<h1>Hello World!</h1>'

# Define um decorador para associar a rota "/home" à função home()
@app.route("/home", methods=['GET', 'POST'])
def home():
    # Define uma variável myvar com o valor 10
    myvar = 10
    # Define uma lista de links
    links = ["http://www.youtube.com", "http://www.python.org", "http://www.https://github.com"]
    # Renderiza o template 'example.html', passando as variáveis myvar e links, e retorna o resultado
    return render_template('example.html', myvar=myvar, links=links)

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento Flask com modo de depuração ativado
    app.run(debug=True)