# coding: utf-8
import sys, getopt, datetime, googlemaps, json
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from config import *
from datetime import datetime

app = Flask('truckpad')

## Dados de acesso ao DB ##
###########################
app.config['MYSQL_HOST'] = HOST
app.config['MYSQL_USER'] = USER
app.config['MYSQL_PASSWORD'] = PASSWORD
app.config['MYSQL_DB'] = DATABASE

mysql = MySQL(app)

## Funções ##
################
# Retorna json do google com dados do endereço
def dados_endereco(endereco):
    gmaps = googlemaps.Client(key=GOOGLE_KEY)
    geocode_result = gmaps.geocode(endereco)
    return geocode_result

# Formata data em d/m/a
def formata_data(data):
    data = datetime.strptime(data, '%Y-%m-%d')
    data = data.strftime('%d/%m/%Y')
    return data

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
            ret.append({'id': d[0], 'nome': d[2], 'cnh':d[1], 'nascimento': formata_data(str(d[3])), 'sexo': d[4], 'tipo_cnh': d[8], 'possui_veiculo': d[6]})

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
                   VALUES ('{}','{}','{}','{}','{}','{}')""".format(_cnh, _nome, _nascimento, _sexo.upper(), _possui_veiculo.upper(), _tipo_cnh)
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
                    WHERE motoristas_cnh='{0}'""".format(_cnh, _nome, _nascimento, _sexo.upper(), _possui_veiculo.upper(), _tipo_cnh)
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return jsonify({'msg':'Motorista atualizado com sucesso'}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        mysql.connection.rollback()
        return jsonify({'msg':'Ocorreu um erro ao fazer o cadastrado - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Retorno de dados do Motorista por CNH
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
            ret.append({'id': d[0], 'nome': d[2], 'cnh':d[1], 'nascimento': formata_data(str(d[3])), 'sexo': d[4], 'tipo_cnh': d[8], 'possui_veiculo': d[6]})

        return jsonify({'total': len(ret), 'dados': ret}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        return jsonify({'msg': 'Ocorreu um erro - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Lista de Trajetos
@app.route('/trajetos/', methods=['GET'])
def lista_trajetos():
    try:
        cur = mysql.connection.cursor()
        query = """SELECT t.trajetos_id, t.trajetos_data, t.trajetos_esta_carregado, t.trajetos_lat_origem, t.trajetos_lng_origem,
                          t.trajetos_lat_destino, t.trajetos_lng_destino, m.motoristas_cnh, m.motoristas_nome, tc.tipo_caminhao_nome,
                          t.trajetos_origem, t.trajetos_destino, t.trajetos_origem_google, t.trajetos_destino_google
                     FROM trajetos t 
                     JOIN motoristas m ON (m.motoristas_id = t.motoristas_id)
                     JOIN tipo_caminhao tc ON (tc.tipo_caminhao_id = t.tipo_caminhao)
                     ORDER BY t.trajetos_data DESC"""
        cur.execute(query)
        dados = cur.fetchall()

        ret = []
        for d in dados:
            ret.append({'id': d[0], 'data': formata_data(str(d[1])), 'carregado':d[2], 'lat_origem': d[3], 'lng_origem': d[4], 'lat_destino': d[5], 'lng_destino': d[6], 'cnh' : d[7], 'nome': d[8], 'tipo_caminhao': d[9], 'endereco_origem': d[10], 'endereco_destino': d[11], 'endereco_origem_google': d[12], 'endereco_destino_google': d[13]})

        return jsonify({'dados': ret, 'total': len(dados)}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        return jsonify({'msg': 'Ocorreu um erro - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Cadastro de Trajetos 
@app.route('/trajeto/', methods=['POST'])
def cadastro_trajeto():
    try:
        dados = request.form
        _cnh = dados.get('cnh', None)
        _data = dados.get('data', None)
        _tipo_caminhao = dados.get('tipo_caminhao', None)
        _carregado = dados.get('carregado', None)
        _endereco_origem = dados.get('endereco_origem', None)
        _endereco_destino = dados.get('endereco_destino', None)
 
        if _cnh is None or _cnh == '':
            return jsonify({'msg': 'Informe a CNH do motorista'}), 412, {"Content-Type": "application/json"}
        if _data is None or _data == '':
            return jsonify({'msg': 'Informe a Data do Trajeto (aaaa-mm-dd)'}), 412, {"Content-Type": "application/json"}
        if _tipo_caminhao is None or _tipo_caminhao == '':
            return jsonify({'msg': 'Informe o Tipo do Caminhão'}), 412, {"Content-Type": "application/json"}
        if _carregado is None or _carregado == '' or _carregado.upper() not in ('S', 'N'):
            return jsonify({'msg': 'Informe se o caminhão está carregado (S/N)'}), 412, {"Content-Type": "application/json"}
        if _endereco_origem is None or _endereco_origem == '':
            return jsonify({'msg': 'Informe o Endereço da Origem'}), 412, {"Content-Type": "application/json"}
        if _endereco_destino is None or _endereco_destino == '':
            return jsonify({'msg': 'Informe o Endereço do Destino'}), 412, {"Content-Type": "application/json"}

        cur = mysql.connection.cursor()
        query = """SELECT motoristas_id 
                     FROM motoristas 
                    WHERE motoristas_cnh = '{}'""".format(_cnh)
        cur.execute(query)
        dados = cur.fetchall()
        motorista_id = dados[0][0]
        
        if motorista_id == '' or motorista_id is None:
            return jsonify({'msg':'Não foi possível identificar motorista'}), 200, {"Content-Type": "application/json"}
         
        end_origem = dados_endereco(_endereco_origem)
        if len(end_origem) > 1:
            return jsonify({'msg':'Foi encontrado mais de um endereço de origem, informe mais detalhes'}), 200, {"Content-Type": "application/json"}

        end_destino = dados_endereco(_endereco_destino)
        if len(end_destino) > 1:
            return jsonify({'msg':'Foi encontrado mais de um endereço de destino, informe mais detalhes'}), 200, {"Content-Type": "application/json"}

        query = """INSERT INTO trajetos (motoristas_id, trajetos_data, tipo_caminhao, trajetos_esta_carregado, trajetos_origem, trajetos_lat_origem, trajetos_lng_origem, trajetos_destino, trajetos_lat_destino, trajetos_lng_destino, trajetos_origem_google, trajetos_destino_google)
                   VALUES ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(motorista_id, _data, _tipo_caminhao, _carregado.upper(), _endereco_origem, end_origem[0]['geometry']['location']['lat'], end_origem[0]['geometry']['location']['lng'], _endereco_destino, end_destino[0]['geometry']['location']['lat'], end_destino[0]['geometry']['location']['lng'], end_origem[0]['formatted_address'], end_destino[0]['formatted_address'])
        cur.execute(query)
        mysql.connection.commit()
        cur.close()
        return jsonify({'msg':'Trajeto cadastrado com sucesso'}), 200, {"Content-Type": "application/json"}
    except Exception as err:
        mysql.connection.rollback()
        return jsonify({'msg':'Ocorreu um erro ao fazer o cadastrado - {}'.format(str(err))}), 500, {"Content-Type": "application/json"}

# Relatorio de totais (Motoristas)
@app.route('/relatorios/totais', methods=['GET'])
def relatorios_totais():
    ret = []
    cur = mysql.connection.cursor()
    query = """SELECT (SELECT count(1) FROM motoristas) as total_motoristas,
                      (SELECT count(1) FROM motoristas WHERE motoristas_possui_veiculo = 'S') as total_possui,
                      (SELECT count(1) FROM motoristas WHERE motoristas_possui_veiculo = 'N') as total_nao_possui
                 FROM dual;"""
    cur.execute(query)
    dados = cur.fetchall()

    for d in dados:
        total_motoristas = d[0]
        total_possui_veiculo = d[1]
        total_nao_possui_veiculo = d[2]

    ret.append({'total_motoristas': total_motoristas, 'total_possui_veiculo': total_possui_veiculo, 'total_nao_possui_veiculo': total_nao_possui_veiculo})
    return jsonify(ret), 200, {"Content-Type": "application/json"}

# Relatório de retorno a origem vazio
@app.route('/relatorios/retornovazio', methods=['GET'])
def relatorios_retornovazio():
    ret = []
    cur = mysql.connection.cursor()
    query = """SELECT m.motoristas_id, m.motoristas_cnh, m.motoristas_nome, t.trajetos_id, t.trajetos_data, t.trajetos_origem, t.trajetos_destino
                 FROM motoristas m
                 JOIN trajetos t ON (t.motoristas_id = m.motoristas_id)
                WHERE trajetos_esta_carregado = 'N'"""
    cur.execute(query)
    dados = cur.fetchall()

    for d in dados:
        ret.append({'motorista_id': d[0], 'cnh': d[1], 'nome':d[2], 'trajeto_id': d[3], 'data': formata_data(str(d[4])), 'endereco_origem': d[5], 'endereco_destino': d[6]})

    return jsonify({'dados': ret, 'total': len(dados)}), 200, {"Content-Type": "application/json"}

# Relatório de caminhoes carregados
#@app.route('/relatorios/carregados', methods=['GET'])
#def relatorios_carregados():

# Relatório de origem e destino agrupado por tipo de caminhao
@app.route('/relatorios/origemdestino', methods=['GET'])
def relatorios_origemdestino():
    ret = []
    cur = mysql.connection.cursor()
    query = """SELECT t.trajetos_id, t.trajetos_data, t.trajetos_origem, t.trajetos_destino, tc.tipo_caminhao_nome, tc.tipo_caminhao_id
                 FROM trajetos t
                 JOIN tipo_caminhao tc ON (tc.tipo_caminhao_id = t.tipo_caminhao)
                GROUP BY tc.tipo_caminhao_nome, t.trajetos_data, t.trajetos_id"""
    cur.execute(query)
    dados = cur.fetchall()

    for d in dados:
        ret.append({'trajetos_id': d[0], 'tipo_caminhao_nome': d[4], 'trajetos_data': formata_data(str(d[1])), 'trajetos_origem': d[2], 'trajetos_destino': d[3]})

    return jsonify({'dados': ret, 'total': len(dados)}), 200, {"Content-Type": "application/json"}

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

