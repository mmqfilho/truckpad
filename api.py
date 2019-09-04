# coding: utf-8
import sys, getopt, datetime
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask('truckpad')

## Dados de acesso ao DB ##
###########################
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'truckpad'

mysql = MySQL(app)

## Rotas da API ##
##################
# Bem vindo
@app.route('/', methods=['GET'])
def index():
    return jsonify({'msg':'API teste Truckpad'}), 200, {"Content-Type": "application/json"}

# Lista de Tipos de CNH
@app.route('/tipocnh/', methods=['GET'])
def lista_tipo_cnh():
    try:
        cur = mysql.connection.cursor()
        query = """SELECT tipo_cnh_id, tipo_cnh_nome 
                     FROM tipo_cnh 
                    ORDER BY 1"""
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'nome': d[1]})

        return jsonify({'total': len(ret), 'dados': ret}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        return jsonify({'msg':'Ocorreu um erro - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Lista de Tipos de Caminhões
@app.route('/tipocaminhao/', methods=['GET'])
def lista_tipo_caminhao():
    try:
        cur = mysql.connection.cursor()
        query = """SELECT tipo_caminhao_id, tipo_caminhao_nome 
                     FROM tipo_caminhao 
                    ORDER BY 1"""
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'nome': d[1]})

        return jsonify({'total': len(ret), 'dados': ret}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        return jsonify({'msg':'Ocorreu um erro - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Lista de Motoristas
@app.route('/motoristas/', methods=['GET'])
def lista_motoristas():
    try:
        cur = mysql.connection.cursor()
        query = """SELECT * 
                     FROM motoristas m 
                     JOIN tipo_cnh t ON (t.tipo_cnh_id = m.tipo_cnh) 
                    ORDER BY 1"""
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'nome': d[2], 'cnh':d[1], 'nascimento': d[3], 'sexo': d[4], 'tipo_cnh': d[8], 'possui_veiculo': d[6]})

        return jsonify({'total': len(ret), 'dados': ret}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        return jsonify({'msg': 'Ocorreu um erro - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Cadastro de Motorista
@app.route('/motorista', methods=['POST'])
def cadastro_motorista():
    try:
        dados = request.form
        _cnh = dados.get('cnh', None)
        _nome = dados.get('nome', None)
        _nascimento = dados.get('nascimento', None)
        _sexo = dados.get('sexo', None)
        _possui_veiculo = dados.get('possui_veiculo', None)
        _tipo_cnh = dados.get('tipo_cnh', None)
        
        if _cnh is None or _cnh == '':
            return jsonify({'msg': 'Informe a CNH do motorista'}), 412, {"Content-Type": "application/json"}
        if _nome is None or _nome == '':
            return jsonify({'msg': 'Informe o Nome do motorista'}), 412, {"Content-Type": "application/json"}
        if _nascimento is None or _nascimento == '':
            return jsonify({'msg': 'Informe a data de nascimento do motorista (aaaa-mm-dd)'}), 412, {"Content-Type": "application/json"}
        if _sexo is None or _sexo == '' or _sexo.upper() not in ('M', 'F'):
            return jsonify({'msg': 'Informe o Sexo do motorista (M/F)'}), 412, {"Content-Type": "application/json"}
        if _possui_veiculo is None or _possui_veiculo == '' or _possui_veiculo.upper() not in ('S', 'N'):
            return jsonify({'msg': 'Informe se o motorista possui veículo (S/N)'}), 412, {"Content-Type": "application/json"}
        if _tipo_cnh is None or _tipo_cnh == '':
            return jsonify({'msg': 'Informe o Tipo da CNH do motorista'}), 412, {"Content-Type": "application/json"}

        cur = mysql.connection.cursor()
        query = """INSERT INTO motoristas (motoristas_cnh, motoristas_nome, motoristas_nascimento, motoristas_sexo, 
                                           motoristas_possui_veiculo, tipo_cnh)
                   VALUES ('{}','{}','{}','{}','{}','{}')""".format(_cnh, _nome, _nascimento, _sexo, _possui_veiculo, _tipo_cnh)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return jsonify({'msg':'Motorista cadastrado com sucesso'}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        mysql.connection.rollback()
        return jsonify({'msg':'Ocorreu um erro ao fazer o cadastrado - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Alteração de Motorista
@app.route('/motorista/<cnh>', methods=['PUT'])
def atualiza_motorista(cnh):
    try:
        dados = request.form
        _cnh = cnh
        _nome = dados.get('nome', None)
        _nascimento = dados.get('nascimento', None)
        _sexo = dados.get('sexo', None)
        _possui_veiculo = dados.get('possui_veiculo', None)
        _tipo_cnh = dados.get('tipo_cnh', None)
        
        if _nome is None or _nome == '':
            return jsonify({'msg': 'Informe o Nome do motorista'}), 412, {"Content-Type": "application/json"}
        if _nascimento is None or _nascimento == '':
            return jsonify({'msg': 'Informe a data de nascimento do motorista (aaaa-mm-dd)'}), 412, {"Content-Type": "application/json"}
        if _sexo is None or _sexo == '' or _sexo.upper() not in ('M', 'F'):
            return jsonify({'msg': 'Informe o Sexo do motorista (M/F)'}), 412, {"Content-Type": "application/json"}
        if _possui_veiculo is None or _possui_veiculo == '' or _possui_veiculo.upper() not in ('S', 'N'):
            return jsonify({'msg': 'Informe se o motorista possui veículo (S/N)'}), 412, {"Content-Type": "application/json"}
        if _tipo_cnh is None or _tipo_cnh == '':
            return jsonify({'msg': 'Informe o Tipo da CNH do motorista'}), 412, {"Content-Type": "application/json"}

        cur = mysql.connection.cursor()
        query = """UPDATE motoristas SET 
                          motoristas_nome='{1}', 
                          motoristas_nascimento='{2}', 
                          motoristas_sexo='{3}', 
                          motoristas_possui_veiculo='{4}', 
                          tipo_cnh='{5}' 
                    WHERE motoristas_cnh='{0}'""".format(_cnh, _nome, _nascimento, _sexo, _possui_veiculo, _tipo_cnh)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return jsonify({'msg':'Motorista atualizado com sucesso'}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        mysql.connection.rollback()
        return jsonify({'msg':'Ocorreu um erro ao fazer o cadastrado - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Retorno de dados do Motorista
@app.route('/motorista/<cnh>', methods=['GET'])
def dados_motorista(cnh):
    try:
        cur = mysql.connection.cursor()
        query = """SELECT * 
                     FROM motoristas m 
                     JOIN tipo_cnh t ON (t.tipo_cnh_id = m.tipo_cnh) 
                    WHERE motoristas_cnh = '{}'""".format(cnh)
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'nome': d[2], 'cnh':d[1], 'nascimento': d[3], 'sexo': d[4], 'tipo_cnh': d[8], 'possui_veiculo': d[6]})

        return jsonify({'total': len(ret), 'dados': ret}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        return jsonify({'msg': 'Ocorreu um erro - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

@app.route('/trajetos/', methods=['GET'])
def lista_trajetos():
    try:
        cur = mysql.connection.cursor()
        query = """SELECT t.trajetos_id, t.trajetos_data, t.trajetos_esta_carregado, t.trajetos_lat_origem, t.trajetos_lng_origem,
                          t.trajetos_lat_destino, t.trajetos_lng_destino, m.motoristas_cnh, m.motoristas_nome, tc.tipo_caminhao_nome
                     FROM trajetos t 
                     JOIN motoristas m ON (m.motoristas_id = t.motoristas_id)
                     JOIN tipo_caminhao tc ON (tc.tipo_caminhao_id = t.tipo_caminhao)
                     ORDER BY t.trajetos_data DESC"""
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'data': d[1], 'carregado':d[2], 'lat_origem': d[3], 'lng_origem': d[4], 'lat_destino': d[5], 'lng_destino': d[6], 'cnh' : d[7], 'nome': d[8], 'tipo_caminhao': d[9]})

        return jsonify({'dados': ret, 'total': len(dados)}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        return jsonify({'msg': 'Ocorreu um erro - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

@app.route('/trajeto/', methods=['POST'])
def cadastro_trajeto():
    try:
        dados = request.form
        _cnh = dados.get('cnh', None)
        _data = dados.get('data', None)
        _tipo_caminhao = dados.get('tipo_caminhao', None)
        _carregado = dados.get('carregado', None)
        _lat_origem = dados.get('lat_origem', None)
        _lng_origem = dados.get('lng_origem', None)
        _lat_destino = dados.get('lat_destino', None)
        _lng_destino = dados.get('lng_destino', None)
        
        if _cnh is None or _cnh == '':
            return jsonify({'msg': 'Informe a CNH do motorista'}), 412, {"Content-Type": "application/json"}
        if _data is None or _data == '':
            return jsonify({'msg': 'Informe a Data do Trajeto (aaaa-mm-dd)'}), 412, {"Content-Type": "application/json"}
        if _tipo_caminhao is None or _tipo_caminhao == '':
            return jsonify({'msg': 'Informe o Tipo do Caminhão'}), 412, {"Content-Type": "application/json"}
        if _carregado is None or _carregado == '' or _carregado.upper() not in ('S', 'N'):
            return jsonify({'msg': 'Informe se o caminhão está carregado (S/N)'}), 412, {"Content-Type": "application/json"}
        if _lat_origem is None or _lat_origem == '':
            return jsonify({'msg': 'Informe a Latitude da Origem'}), 412, {"Content-Type": "application/json"}
        if _lng_origem is None or _lng_origem == '':
            return jsonify({'msg': 'Informe a Longitude da Origem'}), 412, {"Content-Type": "application/json"}
        if _lat_destino is None or _lat_destino == '':
            return jsonify({'msg': 'Informe a Latitude do Destino'}), 412, {"Content-Type": "application/json"}
        if _lng_destino is None or _lng_destino == '':
            return jsonify({'msg': 'Informe a Longitude do Destino'}), 412, {"Content-Type": "application/json"}

        cur = mysql.connection.cursor()
        query = """SELECT motoristas_id 
                     FROM motoristas 
                    WHERE motoristas_cnh = '{}'""".format(_cnh)
        cur.execute(query)
        dados = cur.fetchall()
        motorista_id = dados[0][0]
        
        if motorista_id == '' or motorista_id is None:
            return jsonify({'msg':'Não foi possível identificar motorista'}), 200, {"Content-Type": "application/json"}
                              
        query = """INSERT INTO trajetos (motoristas_id, trajetos_data, tipo_caminhao, trajetos_esta_carregado, trajetos_lat_origem, trajetos_lng_origem, trajetos_lat_destino, trajetos_lng_destino)
                   VALUES ({},'{}','{}','{}','{}','{}','{}','{}')""".format(motorista_id, _data, _tipo_caminhao, _carregado, _lat_origem, _lng_origem, _lat_destino, _lng_destino)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return jsonify({'msg':'Trajeto cadastrado com sucesso'}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        mysql.connection.rollback()
        return jsonify({'msg':'Ocorreu um erro ao fazer o cadastrado - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

    
## Verifica argumentos de linha de comando ##
#############################################
try:
    opts, argv = getopt.getopt(sys.argv[1:], 'p:v', ["port="])
    port = 5000
    for opt, val in opts:
        if opt in ('-p', '--port'):
            port = val
except getopt.GetoptError as err:
    print(err)
    sys.exit()

## Executa API ##
#################
app.run(debug=True, use_reloader=True, port=port)
