# Importa a classe Flask e a função render_template do módulo flask
from flask import Flask, render_template, request

# Cria uma instância da classe Flask, representando a aplicação web
app = Flask(__name__)

# Define um decorador para associar a rota "/" à função index()
@app.route('/')
def index():
    # Renderiza o template 'index.html' e retorna o resultado
    return render_template('index.html')

# Define um decorador para associar a rota "/sign" à função sign()
@app.route('/sign')
def sign():
    # Renderiza o template 'sign.html' e retorna o resultado
    return render_template('sign.html')

# Define um decorador para associar a rota "/process" à função process(), que é acionada por um POST
@app.route('/process', methods=['POST'])
def process():
    # Obtém os dados do formulário submetido pelo método POST
    name = request.form['name']
    comment = request.form['comment']

    # Renderiza o template 'index.html' com as variáveis name e comment, e retorna o resultado
    return render_template('index.html', name=name, comment=comment)

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