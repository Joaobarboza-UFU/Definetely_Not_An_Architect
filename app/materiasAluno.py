from aluno import Aluno as Aluno
from materia import Materia as Materia
from flask import Flask, url_for, request, json, jsonify
from json import dumps
import uuid

class MateriasAluno(object):
    def __init__(self, Aluno, Materias, notas):
        self.__id = uuid.uuid1()
        self.__aluno = Aluno
        self.__materias = Materias
        self.__notas = notas
    
    def getId(self):
        return self.__id

    def getAluno(self):
        return self.__aluno

    def getMaterias(self):
        return self.__materias

    def getNotas(self):
        return self.__notas

    def setAluno(self,aluno):
        self.__aluno = aluno
    
    def setMaterias(self,materias):
        self.__materias = materias

    def setNotas(self,notas):
        self.__notas = notas
    
def createAlunoMateria(myAlunos,myMaterias,myAlunosMaterias):
    req_data = request.get_json()
    aluno_obj = "undefined"
    materia_obj = "undefined"
    flag_aluno = 0
    flag_materia = 0
    notas = req_data['notas']
    for aluno in myAlunos:
         if(str(req_data['id_aluno'].getId()) == str(id)):
             aluno_obj = aluno
             flag_aluno = 1

    for materia in myMaterias:
         if(str(req_data['id_materia'].getId()) == str(id)):
             materia_obj = materia
             flag_materia = 1    
    
    if(flag_aluno == 0):
        msg = "ERRO: Aluno não encontrado"
        return jsonify({'status':msg})
    
    if(flag_materia == 0):
        msg = "ERRO: Matéria não encontrado"
        return jsonify({'status':msg})

    if(len(notas) > 4):
        msg = "ERRO: Número de notas não permitido"
        return jsonify({'status':msg})

    aluno_materia = MateriasAluno(uuid.uuid1(),aluno_obj,materia_obj,notas)
    myAlunosMaterias.append(aluno_materia)

    response = {'status': 'ok'}
    return jsonify(response)
    

def getAlunoMateria(myAlunos,myMaterias,myAlunosMaterias):
    result = []
    average = 0
    for alunoMateria in myAlunosMaterias:
        for nota in alunoMateria.getNotas():
            average+= nota
        average = average/len(alunoMateria.getNotas())

        Aprovado = True if average > 60 else False

        result.append({
            'Nome do estudante': alunoMateria.getAluno.getNome(),
            'Notas': alunoMateria.getNotas(),
            'Média Final': average,
            'Aprovado': str(Aprovado)
        })
    
    return jsonify(result)