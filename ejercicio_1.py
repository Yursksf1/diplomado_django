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

from objetos.nota import Nota
from objetos.materia import Materia
from objetos.estudiante import Estudiante
from objetos.profesor import Profesor

def populate_data():
    '''
    Popular data de la informacion que vamos a trabajar
    return dict {
        'profesores': [<P. sebastian>, <P. luis>, <P. daniel>, ..],
        'estudiantes': [<E. wilson>, <E. walter>, .. ],
    }
    '''

    profesores = []
    estudiantes = []
    materias = []
    notas = []
    
    # --- POPUlAMOS PROFESORES ---
    profesor_1 = Profesor(
        id = 1,
        nombre = 'sebastian henao', 
        lista_materias = ['programacion', 'python']
    )

    profesor_2 = Profesor(
        id = 2,
        nombre = 'luis lopez', 
        lista_materias = ['programacion', 'javascript']
    )

    profesor_3 = Profesor(
        id = 2,
        nombre = 'daniel vargas', 
        lista_materias = ['git', 'html', 'css', 'js']
    )

    profesores.append(profesor_1)
    profesores.append(profesor_2)
    profesores.append(profesor_3)


    # --- POPUlAMOS ESTUDIANTE ---
    estudiante_1 = Estudiante(
        id = 1,
        nombre = 'wilson sanmiguel', 
        lista_materias = ['git', 'python']
    )

    estudiante_2 = Estudiante(
        id = 2,
        nombre = 'walter giovanny', 
        lista_materias = ['programacion', 'html' 'css', 'js']
    )


    estudiantes.append(estudiante_1)
    estudiantes.append(estudiante_2)

    return {
        'profesores': profesores,
        'estudiantes': estudiantes,
        'materias': materias,
        'notas': notas,
    }


# Popular data 
data = populate_data()

# Imprimir valores 
for key, value in data.items():
    print(key, value)
    for val in value:
        print(val.nombre)

print('---- MENU --- ')

a = 1 
index_materia = 1

while (a):
    print('selecciona una opcion: ')

    print('''
    1) Agregar Materia
    9) Imprimir Materia
    0) Salir

    ''')

    a = input('ingresa el dato: ')
    if a == '1':
        # Agregar la materia
        nombre = input('ingresa el nombre de la materia: ')
        materia = Materia(index_materia, nombre)
        data.get('materias').append(materia)

        index_materia = index_materia + 1

        
    if a == '9':
        # Imprimir materias 
        for materia in data.get('materias'):
            print(materia.nombre)

    
print('-- se acabo de ejecutar todo el codigo--')
