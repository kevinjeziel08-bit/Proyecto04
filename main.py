class Alumnos:
    def __init__(self, nombre, matricula, calificaciones):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = calificaciones

lista_de_alumnos = []
matriz_calificaciones = []

num_alumnos = int(input("Cuantos estudiantes vas a ingresar? "))
num_materias = int(input("Cuantas calificaciones tiene cada estudiante? "))

for i in range(num_alumnos):
    print(f"Datos del alumno {i + 1}")
    nombre = input("Nombre: ")
    matricula = input("Matricula: ")

    calificaciones_alumnos = []
    for j in range(num_materias):
        calificaciones = int(input(f"Calificaciones {j + 1}: "))
        calificaciones_alumnos.append(calificaciones)

    matriz_calificaciones.append(calificaciones_alumnos)

    nuevo_alumno = Alumnos(nombre, matricula, calificaciones_alumnos)
    lista_de_alumnos.append(nuevo_alumno)

promedio = []

for i in range(len(lista_de_alumnos)):
    suma_alumno = 0

    for j in range(len(matriz_calificaciones[i])):
        suma_alumno = suma_alumno + matriz_calificaciones[i][j]

    promedio_alumno = suma_alumno / num_materias
    promedio.append(promedio_alumno)

    print()

    print(f"Alumno: {lista_de_alumnos[i].nombre} | Matricula: {lista_de_alumnos[i].matricula} | Calificaciones: {lista_de_alumnos[i].calificaciones} | Promedio: {promedio_alumno:.2f}")

general = 0
promedio_mayor = promedio[0]
promedio_menor = promedio[0]

for prom in promedio:
    general = general + prom

    if prom > promedio_mayor:
        promedio_mayor = prom

    if prom < promedio_menor:
        promedio_menor = prom

promedio_general = general / len(promedio)

print()
print(f"Promedio mayor del grupo: {promedio_mayor:.2f}.")
print(f"Promedio menor del grupo: {promedio_menor:.2f}.")
print(f"Promedio general del grupo: {promedio_general:.2f}.")
