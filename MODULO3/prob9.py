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

    prom=(nota1+nota2+nota3)/3
    contar=0
    desa=0
    if prom>=4:
        contar+=contar
    else:
        desa+=desa

print("Total de estudiantes aprobados: {}".format(contar))
print("Total de estudiantes desaprobados: {}".format(desa))