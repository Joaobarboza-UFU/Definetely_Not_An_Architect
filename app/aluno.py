from user import User
from flask import Flask, url_for, request, json, jsonify
from json import dumps
import uuid

class Aluno(User):
    def __init__(self, id, nome, idade, cidade, serie, coeficienteAcademico, materiasEmAndamento):
        self.__id = uuid.uuid1()
        self.__nome = nome        
        self.__idade = idade
        self.__cidade = cidade  
        self.__Serie = serie
        self.__CoeficienteAcademico = coeficienteAcademico
        self.__MateriasEmAndamento = materiasEmAndamento

    def getSerie(self):
        return self.__Serie

    def getCoeficienteAcademico(self):
        return self.__CoeficienteAcademico

    def getMateriasEmAndamento(self):
        return self.__MateriasEmAndamento

    def setSerie(self,serie):
        self.__Serie = serie
        return self

    def setCoeficienteAcademico(self,coeficienteAcademico):
        self.__CoeficienteAcademico = coeficienteAcademico
        return self

    def setMateriasEmAndamento(self,materiasEmAndamento):
        self.__MateriasEmAndamento = materiasEmAndamento
        return self

def createAluno(myAlunos):
    req_data = request.get_json()
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    serie = req_data['serie']
    coeficienteAcademico = req_data['CRA']
    materiasEmAndamento = req_data['materias']
    aluno = Aluno(uuid.uuid1(),nome, idade, cidade, serie, coeficienteAcademico, materiasEmAndamento)
    myAlunos.append(aluno)
    response = {'status': 'ok'}
    return jsonify(response)

def getAluno(myAlunos):
    result = []
    for aluno in myAlunos:
        result.append({
            'id':aluno.getId(),
            'idade':aluno.getIdade(),
            'nome':aluno.getNome(),
            'cidade':aluno.getCidade(),
            'serie':aluno.getSerie(),
            'CRA':aluno.getCoeficienteAcademico(),
            'Materias':aluno.getMateriasEmAndamento()
        })
    return jsonify(result)

def alterAluno(myAlunos,id):
    req_data = request.get_json()

    for aluno in myAlunos:
        if(str(aluno.getId()) == str(id)):
            aluno.setNome(req_data['nome'] if "nome" in req_data else aluno.getNome())
            aluno.setIdade(req_data['idade'] if "idade" in req_data else aluno.getIdade())
            aluno.setCidade(req_data['cidade'] if "cidade" in req_data else aluno.getCidade())
            aluno.setSerie(req_data['serie'] if "serie" in req_data else aluno.getSerie())
            aluno.setCoeficienteAcademico(req_data['CRA'] if "CRA" in req_data else aluno.getCoeficienteAcademico())
            aluno.setMateriasEmAndamento(req_data['materias'] if "materias" in req_data else aluno.getMateriasEmAndamento())
            return jsonify({'status': 'Usuário Alterado'})

    return jsonify({'status': 'ERRO: Usuário Não Encontrado'})

def deleteAluno(myAlunos,id):
    for index,aluno in enumerate(myAlunos):
        if(str(aluno.getId()) == str(id)):
            myAlunos.pop(index)
            return jsonify({'status': 'Usuário Removido'})
    
    return jsonify({'status': 'ERRO: Usuário Não Encontrado'})
