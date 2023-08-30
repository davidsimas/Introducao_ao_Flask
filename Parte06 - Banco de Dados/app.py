# Importa a classe Flask do módulo flask
from flask import Flask, render_template, request, redirect, url_for
# Importa a classe SQLAlchemy do módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do SQLAlchemy
db = SQLAlchemy()
# Cria uma instância da classe Flask, representando a aplicação web
app = Flask(__name__)
# Configura o banco de dados SQLite, relativo à pasta de instância da aplicação
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializa a aplicação com a extensão SQLAlchemy
db.init_app(app)

# Define o modelo "Comments" representando a tabela no banco de dados
class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))

# Cria todas as tabelas definidas no modelo no banco de dados
with app.app_context():
    db.create_all()

# Define um decorador para associar a rota "/" à função index()
@app.route('/')
def index():
	# Obtém todos os registros da tabela "Comments"
	result = Comments.query.all()
	# Renderiza o template 'index.html' passando os resultados e retorna o resultado
	return render_template('index.html', result=result)

# Define um decorador para associar a rota "/sign" à função sign()
@app.route('/sign')
def sign():
    # Renderiza o template 'sign.html' e retorna o resultado
    return render_template('sign.html')

# Define um decorador para associar a rota "/process" à função process(), acionada por um POST
@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']
	# Cria uma instância do modelo "Comments"
	signature = Comments(name=name, comment=comment)
	# Adiciona a instância ao banco de dados
	db.session.add(signature)
	# Confirma a adição no banco de dados
	db.session.commit()
	# Redireciona para a página index
	return redirect(url_for('index'))

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