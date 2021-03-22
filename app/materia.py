from user import User
from flask import Flask, url_for, request, json, jsonify
from json import dumps
from professor import Professor as Professor
import uuid

class Materia(object):
    def __init__(self, id, nome, horas, professor):
        self.__id = uuid.uuid1()
        self.__nome = nome        
        self.__horas = horas
        self.__professor = professor

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getHoras(self):
        return self.__horas

    def getProfessor(self):
        return self.__professor

    def setNome(self,nome):
        self.__nome = nome
        return self

    def setHoras(self, horas):
        self.__horas = horas
        return self

    def setProfessor(self, professor):
        self.__professor = professor
        return self

def createMateria(myMaterias):
    req_data = request.get_json()

    id = uuid.uuid1()
    nome = req_data['nome']
    horas = req_data['horas']
    professor = req_data['professor']
    materia = Materia(id, nome, horas, professor)
    myMaterias.append(materia)
    response = {'status': 'ok'}
    return jsonify(response)

def getMaterias(myMaterias):
    result = []
    for materia in myMaterias:
        result.append({
            'id': str(materia.getId()),
            'nome': str(materia.getNome()),
            'horas': str(materia.getHoras()),
            'professor': str(materia.getProfessor())
        })
    return jsonify(result)

def alterMateria(myMaterias,id):
    req_data = request.get_json()
    for materia in myMaterias:
        if(str(materia.getId()) == str(id)):
            materia.setNome(req_data['nome'] if "nome" in req_data else materia.getNome())
            materia.setHoras(req_data['horas'] if "horas" in req_data else materia.getHoras())
            materia.setProfessor(req_data['professor'] if "professor" in req_data else materia.getProfessor())
            return jsonify({'status': 'Matéria Alterada'})

    return jsonify({'status': 'ERRO 404: Matéria Não Encontrada'})

def deleteMateria(myMaterias,id):
    for index, materia in enumerate(myMaterias):
        if(str(materia.getId()) == str(id)):
            myMaterias.pop(index)
            return jsonify({'status': 'Matéria Removida'})
    
    return jsonify({'status': 'ERRO 404: Matéria Não Encontrado'})
