# coding: utf-8
import sys, getopt, datetime
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask('truckpad')

## Dados de acesso ao DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'truckpad'

mysql = MySQL(app)

## Rotas
@app.route('/', methods=['GET'])
def index():
    return jsonify({'msg':'API teste Truckpad'}), 200, {"Content-Type": "application/json"}

@app.route('/tipocnh/', methods=['GET'])
def lista_tipo_cnh():
     try:
         cur = mysql.connection.cursor()
         query = "SELECT tipo_cnh_id, tipo_cnh_nome FROM tipo_cnh ORDER BY 1"
         cur.execute(query)
         dados = cur.fetchall()

         ret = []
         for d in dados:
             ret.append({'id': d[0], 'nome': d[1]})

         return jsonify({'dados': ret}), 200, {"Content-Type": "application/json"}
     except:
         return jsonify({'msg':'Ocorreu um erro'}), 500, {"Content-Type": "application/json"}

@app.route('/tipocaminhao/', methods=['GET'])
def lista_tipo_caminhao():
     try:
         cur = mysql.connection.cursor()
         query = "SELECT tipo_caminhao_id, tipo_caminhao_nome FROM tipo_caminhao ORDER BY 1"
         cur.execute(query)
         dados = cur.fetchall()

         ret = []
         for d in dados:
             ret.append({'id': d[0], 'nome': d[1]})

         return jsonify({'dados': ret}), 200, {"Content-Type": "application/json"}
     except:
         return jsonify({'msg':'Ocorreu um erro'}), 500, {"Content-Type": "application/json"}

@app.route('/motoristas/', methods=['GET'])
def lista_motoristas():
    try:
        cur = mysql.connection.cursor()
        query = "SELECT * FROM motoristas m JOIN tipo_cnh t ON (t.tipo_cnh_id = m.tipo_cnh) ORDER BY 1"
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'nome': d[2], 'cnh':d[1], 'nascimento': d[3], 'sexo': d[4], 'tipo_cnh': d[8], 'possui_veiculo': d[6]})

        return jsonify({'dados': ret, 'total': len(dados)}), 200, {"Content-Type": "application/json"}
    except:
        return jsonify({'msg': 'Ocorreu um erro'}), 500, {"Content-Type": "application/json"}

@app.route('/motorista', methods=['POST'])
def cadastro_motorista():
    try:
        dados = request.form
        _cnh = dados['cnh']
        _nome = dados['nome']
        _nascimento = dados['nascimento']
        _sexo = dados['sexo']
        _possui_veiculo = dados['possui_veiculo']
        _tipo_cnh = dados['tipo_cnh']

        lista_possui_veiculo = ['S', 'N']
        if _possui_veiculo not in lista_possui_veiculo:
            return jsonify({'msg': 'Resposta "Possui veículo" inválido'}), 412, {"Content-Type": "application/json"}

        cur = mysql.connection.cursor()
        query = """INSERT INTO motoristas(motoristas_cnh, motoristas_nome, motoristas_nascimento, motoristas_sexo, 
                               motoristas_possui_veiculo, tipo_cnh)
                       VALUES ('{}','{}','{}','{}','{}','{}')""".format(_cnh, _nome, _nascimento, _sexo, _possui_veiculo, _tipo_cnh)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return jsonify({'msg':'Motorista cadastrado com sucesso'}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        mysql.connection.rollback()
        return jsonify({'msg':'Ocorreu um erro ao fazer o cadastrado - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

@app.route('/motorista/<cnh>', methods=['PUT'])
def atualiza_motorista(cnh):
    try:
        dados = request.form
        _cnh = cnh
        _nome = dados['nome']
        _nascimento = dados['nascimento']
        _sexo = dados['sexo']
        _possui_veiculo = dados['possui_veiculo']
        _tipo_cnh = dados['tipo_cnh']

        lista_possui_veiculo = ['S', 'N']
        if _possui_veiculo not in lista_possui_veiculo:
            return jsonify({'msg': 'Resposta "Possui veículo" inválido'}), 412, {"Content-Type": "application/json"}

        cur = mysql.connection.cursor()
        query = """UPDATE motoristas SET motoristas_nome='{1}', motoristas_nascimento='{2}', motoristas_sexo='{3}', 
                   motoristas_possui_veiculo='{4}', tipo_cnh='{5}' WHERE motoristas_cnh='{0}'""".format(_cnh, _nome, _nascimento, _sexo, _possui_veiculo, _tipo_cnh)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return jsonify({'msg':'Motorista atualizado com sucesso'}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        mysql.connection.rollback()
        return jsonify({'msg':'Ocorreu um erro ao fazer o cadastrado- {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

@app.route('/trajetos/', methods=['GET'])
def lista_trajetos():
    try:
        cur = mysql.connection.cursor()
        query = "SELECT * FROM trajetos ORDER BY 1"
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'nome': d[2], 'cnh':d[1], 'nascimento': d[3], 'sexo': d[4], 'tipo_cnh': d[8], 'possui_veiculo': d[6]})

        return jsonify({'dados': ret, 'total': len(dados)}), 200, {"Content-Type": "application/json"}
    except:
        return jsonify({'msg': 'Ocorreu um erro'}), 500, {"Content-Type": "application/json"}

## verifica argumentos de linha de comando
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
