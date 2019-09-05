# truckpad
teste python da truckpad

1 - Módulos a serem instalados via pip\
pip install -r requirements.txt

1.1 - Erro de pacote na instalação no windows\
Caso seja usado o ambiente windows, pode ocorrer um erro na instalação de pacote de dependências do mysqlclient, neste caso:
* baixar a versão correta em https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
* instalar o wheel (pip install wheel)
* instalar o mysqlclient (pip install mysqlclient-1.4.4-cp37-cp37m-win32.whl - ver o nome correto baixado)
* executar novamente o passo 1 (pip install -r requirements.txt)

2 - Arquivos a serem importados para banco de dados\
install.sql

2.1 - Atualizar dados de acesso ao banco\
No arquivo config.py atualizar as variáveis abaixo:\
HOST\
DATABASE\
USER\
PASSWORD

3 - Google api\
No arquivo config.py atualizar a variável abaixo:\
GOOGLE_KEY

4 - Executar arquivo para iniciar api\
python api.py

5 - Utilizar programa Postman para trabalhar com a API:\
Importar o arquivo truckpad.postman_collection.json e utilizar os serviços disponíveis
