#2PROBLEMA DE NOTAS

cantidad=int(input('Ingrese el número de estudiantes: '))
names=[]
notes=[]
for x in range(cantidad):
    nom=input("Ingrese el nombre del alumno:")
    names.append(nom)
    nota1=int(input("Ingrese la primer nota:"))
    nota2=int(input("Ingrese la segunda nota:"))
    nota3=int(input("Ingrese la tercera nota:"))
    notes.append([nota1,nota2,nota3])

for x in range(cantidad):
    print(names[x],notes[x][0],notes[x][1],notes[x][2])
