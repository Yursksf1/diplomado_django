'''
1) Implementar la logica de una institucion educativa.

Profesores
Estudiantes
Materias
Notas
Horarios de Clase (*opcional)
estas entidades deben ser implementadas mediante objetos. el programa debe permitir las siguientes funciones:

1) un profesor debe poder ver las materias que tienen asignadas (un profesor puede dictar varias clases pero debe al menos dar una)

2) Una materia puede ser dictada por varios profesores y pueden estar inscritos varios estudiantes

3) un estudiante puede estar inscritos en muchas materias

4) las notas son ingresadas por el profesor que dicta la materia en la clase donde el estudiante este incrito

5) los estudiantes deben poder ver que notas tienen y ver un promedio por materia y general en todas sus materias

6) {OPCIONAL} - los horarios son definidos de maximo 6 horas diarias, un estudiante no puede estar en dos materias con el mismo horario, un profesor no puede dictar dos materias que sean vistas el mismo

'''


class Profesor():
    id = ''
    nombre = ''
    lista_materias = []
    

class Estudiante():
    id = ''
    nombre = ''
    lista_materias = []
    

class Materia():
    id = ''
    nombre = ''
    horario = ''

class Nota():
    id_materia = ''
    valor = ''