# in this class define relations clasess


class profesor_materia():
    def __init__(id_profesor, id_materia):
        self.id_profesor = id_profesor
        self.id_materia = id_materia


class estudiante_materia():
    def __init__(id_estudiante, id_materia):
        self.id_estudiante = id_estudiante
        self.id_materia = id_materia


class estudiante_materia_nota():
    def __init__(id_profesor, id_materia, id_nota):
        self.id_profesor = id_profesor
        self.id_materia = id_materia
        self.id_nota = id_nota