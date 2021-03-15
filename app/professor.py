from user import User

class Professor(User):
    __id = None
    __nome = None    
    __idade = None
    __cidade = None
    __graduacao = None
    __horasSemanais = None


    def __init__(self, id, nome, idade, cidade, graduacao, horasSemanais):
        self.__id = id
        self.__nome = nome        
        self.__idade = idade
        self.__cidade = cidade  
        self.__graduacao = graduacao
        self.__horasSemanais = horasSemanais

    def getProfessorGraduacao(self):
        return self.__graduacao

    def getProfessorHorasSemanais(self):
        return self.__horasSemanais

    def setProfessorGraduacao(self,graduacao):
        self.__graduacao = graduacao
        return self

    def setProfessorHorasSemanais(self,horasSemanais):
        self.__horasSemanais = horasSemanais
        return self

    def getProfessor(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self
        else:
            retorno = "Professor nao encontrado!!"
        return (retorno)
