
#PROBLEMA4
cantidad=int(input('Ingrese la cantidad de alumnos: '))
names=[]
notes=[]
suma=0
for x in range(cantidad):
    nom=input("Ingrese el nombre del alumno:")
    names.append(nom)
    nota1=int(input("Ingrese la primer nota:"))
    nota2=int(input("Ingrese la segunda nota:"))
    nota3=int(input("Ingrese la tercera nota:"))
    notes.append([nota1,nota2,nota3])
    prom=(nota1+nota2+nota3)/3
    suma=suma+prom

for x in range(cantidad):
    print(names[x],notes[x][0],notes[x][1],notes[x][2])
promtotal=suma/cantidad
print('El promedio total del salon es: {}'.format(promtotal))