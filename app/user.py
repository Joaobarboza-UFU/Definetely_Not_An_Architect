import uuid
from flask import Flask, url_for, request, json, jsonify
from json import dumps

class User(object):
    def __init__(self, id, nome, idade, cidade):
        self.__id = uuid.uuid1()
        self.__nome = nome        
        self.__idade = idade
        self.__cidade = cidade

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getCidade(self):
        return self.__cidade

    def setNome(self,nome):
        self.__nome = nome
        return self

    def setCidade(self,cidade):
        self.__cidade = cidade
        return self        

    def getUserName(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "usuario nao encontrado!!"
        return (retorno)
