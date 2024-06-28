
def calcular_promedio(notas):
    cantidad_notas = len(notas)
    total = 0

    if(cantidad_notas>0):
        for nota in notas:
            total += nota
        promedio = total/cantidad_notas
        return round(promedio,2)

    else:
        return 'No tiene notas almacenadas'


def determinar_estado(promedio):
    if promedio == 'No tiene notas almacenadas':
        return '-'
    elif promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"
    

def crear_lista_notas(cadena_texto):
    lista_notas = []
    notas = cadena_texto.split(',')

    for nota in notas:
        try:
            nota_int = int(nota.strip())
            lista_notas.append(nota_int)
        except ValueError:
            # Si no se puede convertir a entero, simplemente pasa a la siguiente nota
            pass

    return lista_notas



notas_estudiantes = {}
proceso_almacenamiento_activado = True

# Solicitamos y almacenamos información de los estudiantes
while(proceso_almacenamiento_activado):
    nombre_estudiante = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")

    if(nombre_estudiante == 'salir'):
        proceso_almacenamiento_activado = False
        break
    
    cadena_notas_estudiante = input("Ingrese las notas del estudiante separadas por coma: ")

    lista_notas_estudiante = crear_lista_notas(cadena_notas_estudiante)

    notas_estudiantes.update({nombre_estudiante:lista_notas_estudiante})

# Creamos listado con nombres de estudiantes a partir del objeto que contiene las notas
nombres_estudiantes = [nombre for nombre in notas_estudiantes.keys()]

# Recorremos el listado de estudiantes, calculando sus promedios y determinando estado
if(len(nombres_estudiantes)>0):
    for estudiante in nombres_estudiantes:
        promedio_estudiante = calcular_promedio(notas_estudiantes[estudiante])
        estado = determinar_estado(promedio_estudiante)
        print(f'Promedio de notas de {estudiante}: {promedio_estudiante}, Estado: {estado}')
else:
    print('No se han agregado estudiantes')

