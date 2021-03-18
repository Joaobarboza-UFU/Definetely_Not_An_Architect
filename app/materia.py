class Materia(object):
    __id = None
    __nome = None    
    __horas = None
    __professor = None

    def __init__(self, id, nome, horas, professor):
        self.__id = id
        self.__nome = nome        
        self.__horas = horas
        self.__professor = professor

    def getCourseId(self):
        return self.__id

    def getCourseNome(self):
        return self.__nome

    def getCourseHoras(self):
        return self.__horas

    def getCourseProfessor(self):
        return self.__professor

    def setCourseNome(self,nome):
        self.__nome = nome
        return self

    def setCourseHoras(self, horas):
        self.__horas = horas
        return self

    def setCourseProfessor(self, professor):
        self.__professor = professor
        return self

    def getCourse(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self
        else:
            retorno = "Course not found!!"
        return (retorno)
