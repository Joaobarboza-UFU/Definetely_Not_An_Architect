from user import User

class Aluno(User):
    __id = None
    __nome = None    
    __idade = None
    __cidade = None
    __Serie = None
    __CoeficienteAcademico = None
    __MateriasEmAndamento = None


    def __init__(self, id, nome, idade, cidade, serie, coeficienteAcademico, materiasEmAndamento):
        self.__id = id
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

    def getProfessor(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self
        else:
            retorno = "Professor nao encontrado!!"
        return (retorno)
