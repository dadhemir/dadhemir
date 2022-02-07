import os
# path principal
ppal = "C:/Users/dadhemir/OneDrive - bucaramanga.gov.co/DiegoAdemirDuarteSantana--Labor2021/"
# número de obligación
numobl = str(input ("Ingrese el número de obligación: "))
# número de informe
#numinfo = str(input ("Ingrese el número de informe: "))
# path mejorado
#ppal = ppal + "Obligación" + numobl + "/" + "Informe" + numinfo
ppal = ppal + "Obligación" + numobl
# listar archivos
print ("Listado de Archivos:")
i=0
for root, dirs, files in os.walk(ppal):
    for filename in files:
        #print(str(i) + " " + filename)
        print(filename)
        i+=1
print("Total de archivos: " + str(i))