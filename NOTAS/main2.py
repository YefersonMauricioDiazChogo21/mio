from alumnos2 import *

menu = "BIENVENIDOS AL SISTEMA DE NOTAS\n\tINGRESE EL NUMERO DE LA OPCION QUE DESEA EJECUTAR\n\t1. AGREGAR ALUMNO\n\t2. AGREGAR NOTAS\n\t3. BUSCAR ALUMNO\n\t4. SALIR"
intError = True
opcion = 0
def menuInstituto() -> int:
    global intError, opcion
    opcion = 0
    intError = True
    print(menu)
    while (intError == True):
        try:
            opcion += int(input("\t-_o "))
            return opcion
        except ValueError:
            intError = True
alv = True
while alv:
    menuInstituto()
    if opcion == 1:
        agregarAlumnos()
        alv = True
    elif opcion == 2:
        agregarNotas()
        alv = True
    elif opcion == 3:
        verAlumno()
        alv = True
    elif opcion == 4:
        # cierre
        alv = False
    else:
        print("opcion no valida -_-")
        alv = True