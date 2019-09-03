# coding: utf-8
import sys, getopt
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask('truckpad')

## Dados de acesso ao DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'truck'

mysql = MySQL(app)

## Rotas
@app.route('/', methods=['GET'])
def index():
    return {'msg':'API teste Truckpad'}, 200, {"Content-Type": "application/json"}
    
@app.route('/motorista/', methods=['POST']):
def cadastro_motorista():
    try:
        dados = request.form
        _cnh = dados['cnh']
        _nome = dados['nome']
        _nascimento = dados['nascimento']
        _sexo = dados['sexo']
        _possui_veiculo = dados['possui_veiculo']
        _tipo_cnh = dados['tipo_cnh']
    
        cur = mysql.connection.cursor()
        query = "INSERT INTO () VALUES ('{}','{}','{}','{}','{}','{}')".format(_cnh, _nome, _nascimento, _sexo, _possui_veiculo, _tipo_veiculo)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return {'msg':'Motorista cadastrado com sucesso'}, 200, {"Content-Type": "application/json"}
    except:
        mysql.connection.rollback()
        return {'msg':'Ocorreu um erro ao fazer o cadastrado'}, 500, {"Content-Type": "application/json"}
    
@app.route('/motorista/<cnh>', methods=['PUT']):
def atualiza_motorista(cnh):
    try:
        dados = request.form
        _cnh = cnh
        _nome = dados['nome']
        _nascimento = dados['nascimento']
        _sexo = dados['sexo']
        _possui_veiculo = dados['possui_veiculo']
        _tipo_cnh = dados['tipo_cnh']
        
        cur = mysql.connection.cursor()
        query = "UPDATE SET ='{1}', ='{2}', ='{3}', ='{4}', ='{5}' WHERE cnh='{0}'".format(_cnh, _nome, _nascimento, _sexo, _possui_veiculo, _tipo_veiculo)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return {'msg':'Motorista cadastrado com sucesso'}, 200, {"Content-Type": "application/json"}
    except:
        mysql.connection.rollback()
        return {'msg':'Ocorreu um erro ao fazer o cadastrado'}, 500, {"Content-Type": "application/json"}
 
## verifica argumentos 
try:
    opts, argv = getopt.getopt(sys.argv[1:], 'p:v', ["port="])
    port = 5000
    for opt, val in opts:
        if opt in ('-p', '--port'):
            port = val

except getopt.GetoptError as err:
    print(err)
    sys.exit()

# executa API    
app.run(debug=True, use_reloader=True, port=port)
