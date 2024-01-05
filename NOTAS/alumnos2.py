cont = 0
listaAlumno =[]
alnValue = True
subMenuNotas = "REGISTRO DE NOTAS\n\t1. AGREGAR NOTA DEL PARCIAL\n\t2. AGREGAR NOTAS DE LOS QUIZES\n\t3. AGREGAR NOTAS DE LOS TRABAJOS\n\t4. VOLVER AL MENU PRINCIPAL"
intError = True
opcion2 = 0

def agregarAlumnos():
    global cont, listaAlumno
    cont = 0
    alnValue = True
    stop = True

    print("INFORMACION DEL ALUMNO")
    numDoc = input("1. INGRESE EL NUMERO DE DOCUMENTO DEL ALUMNO\n\t")
    for i in range(0,cont):
        if listaAlumno[i]== numDoc:
            print("Alumno ya esta registrado -_-")
    cont += 1
    nombre = input("2. INGRESE EL NUMERO DE NOMBRE COMPLETO DEL ALUMNO\n\t")
    edad = input("3. INGRESE LA EDAD DEL ALUMNO\n\t")
    alumno = [numDoc, nombre, edad,[],[],[],[],[],[]]       #las listas son para almacenar los siguientes valores,
                                                            #nota parcial, notas de quices, notas de trabajos,
                                                            #promedio de quices, promedio de trabajos y promedio total respectivamente 
    listaAlumno.append(alumno)
notaParcial=0          
def agregarNotas():
    global listaAlumno, notaParcial
    print(listaAlumno[0])
    Id = int(input("INGRESE EL DOCUMENTO DEL ALUMNO AL CUAL LE DESEA AGREGAR LAS NOTAS\n\t"))
    cont = 0
    for i in range(0):
        if Id != listaAlumno[i][0] :
            cont +=1
            continue
        else:
            break
    print(listaAlumno[cont][1])
    global intError, opcion2
    opcion2 = 0
    intError = True
   
    while intError == True:
        print(subMenuNotas)
        opcion2 = int(input("\t-_o "))
        if opcion2 == 1:
            print("Deves sacar almenos 3.6 para aprovar")
            listaAlumno[cont][3] = float(input("INGRESE LA NOTA DEL PARCIAL (0-5)\n\t"))
            intError = True
            print(listaAlumno[cont][3]) 
        elif opcion2 == 2:
            quizSuma = 0
            con2 = 0
            notaQuiz = float(input("INGRESE LA NOTA DEl QUIZ (0-5)\n\t"))
            listaAlumno[cont][4].append(notaQuiz)
            for i in listaAlumno[cont][4]:
                quizSuma += i
                con2+=1
            promedioQuiz = quizSuma/con2
            notaQuizNesesaria = 7.2-promedioQuiz
            listaAlumno[cont][6] = notaQuizNesesaria
            print("NECESITAS ALMENOS ", notaQuizNesesaria, " EN TU/TUS SIGUIENTE/S QUIZ/QUICES PARA APROVAR")
            intError = True
        elif opcion2 == 3:
            trabajosSuma =0
            con3 =0
            notaTrabajo = float(input("INGRESE LA NOTA DEL TRABJO (0-5)\n\t"))
            listaAlumno[cont][5].append(notaTrabajo)
            for i in listaAlumno[cont][5]:
                trabajosSuma += i
                con3+=1
            promedioTrabajos = trabajosSuma/con3
            notaTrabajosNesesaria = 7.2-promedioTrabajos
            listaAlumno[cont][7] = notaTrabajosNesesaria
            print("NECESITAS ALMENOS ", notaTrabajosNesesaria, " EN TU/TUS SIGUIENTE/S TRABAJO/S PARA APROVAR")
            intError = True
        elif opcion2 == 4:
            # cierre
            intError = False
        else:
            print("opcion no valida -_-")
            intError = True

    


def verAlumno():
    cont =0
    global listaAlumno
    print("VISUALIZACION DE LOS ALUMNOS Y SUS DATOS")
    Id = input("INGRESE EL NUMERO DE DOCUMENTO DE EL ALUMNO\n\t")
    for i in range(0):
        if Id != listaAlumno[i][0] :
            cont +=1
            continue
        else:
            cont =0
    

