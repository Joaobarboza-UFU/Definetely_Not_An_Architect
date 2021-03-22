from flask import Flask, url_for, request, json, jsonify
from json import dumps
from user import User
import aluno as Aluno
import materia as Materia
import materiasAluno as MateriasAluno

app = Flask(__name__)
myUser = []
myAlunos = []
myMaterias = []
myAlunosMaterias = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'

@app.route('/hello')
def api_hello(): 
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:        
        return 'Hello John Doe'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
@app.route('/createuser')
def api_createuser():
    global myUser
    myUser.append(User(1, "Joao", 12, "São Paulo"))
    myUser.append(User(2, "Pedro",  13, "São Tomé"))
    myUser.append(User(3, "Jorge",  14, "São Bernardo"))
    myUser.append(User(4, "Valdir",  11, "São Roque"))
    myUser.append(User(5, "Antonio",  10, "São Cristóvão"))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/getuser', methods = ['GET']) 
def api_getuser():
    global myUser
    user_data = request.get_json() 
    print(user_data)
    codUser = user_data['codigo']
    print(codUser)
    print(myUser[0].getUserNome())
    res = {'status': 'usuario nao encontrado'}
    for elem in myUser:
        if(int(codUser) == elem.getUserId()):
            res = {'nome': elem.getUserNome()}
        
    return jsonify(res)

@app.route('/adduser', methods = ['POST'])
def api_newuser():
    global myUser
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    new_user = User(id, nome, idade, cidade)
    myUser.append(new_user)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/listusers', methods = ['GET'])
def api_listusers():
    global myUser
    payload = []
    content = {}
    
    for elem in myUser:        
        content = {'id': str(elem.getUserId()),
                   '[nome]': elem.getUserNome(), 
                   '[idade]': str(elem.getUserIdade()), 
                   '[cidade]': elem.getUserCidade()}
        payload.append(content)
        content = {}

    res =  json.dumps(payload)       
    res =  payload       
    
    return jsonify(res)

    
@app.route('/aluno', methods = ['GET'])
def api_getaluno():
    global myAlunos
    return Aluno.getAluno(myAlunos)

@app.route('/aluno', methods = ['POST'])
def api_createaluno():
    global myAlunos
    return Aluno.createAluno(myAlunos)

@app.route('/aluno/<id>', methods = ['PUT'])
def api_alteraluno(id):
    global myAlunos
    return Aluno.alterAluno(myAlunos,id)
        
@app.route('/aluno/<id>', methods = ['DELETE'])
def api_deletealuno(id):
    global myAlunos
    return Aluno.deleteAluno(myAlunos,id)

@app.route('/materia', methods = ['GET'])
def api_getdisciplina():
    global myDisciplinas
    return Materia.getMaterias(myMaterias)

@app.route('/materia', methods = ['POST'])
def api_createdisciplina():
    global myDisciplinas
    return Materia.createMateria(myMaterias)

@app.route('/materia/<id>', methods = ['PUT'])
def api_altdisciplina(id):
    global myDisciplinas
    return Materia.alterMateria(myMaterias,id)

@app.route('/materia/<id>', methods = ['DELETE'])
def api_deletedisciplina(id):
    global myDisciplinas
    return Materia.deleteMateria(myMaterias,id)

@app.route('/aluno/materia', methods = ['GET'])
def api_getalunodisciplina():
    global myAlunos
    global myDisciplinas
    global myAlunosDisciplinas
    return MateriasAluno.getAlunoMateria(myAlunos,myMaterias,myAlunosMaterias)

@app.route('/aluno/materia', methods = ['POST'])
def api_createalunodisciplina():
    global myAlunos
    global myDisciplinas
    global myAlunosDisciplinas
    return MateriasAluno.createAlunoMateria(myAlunos,myMaterias,myAlunosMaterias)

if __name__ == '__main__':
    app.run()