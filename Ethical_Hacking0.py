import sys,os
import random
from array import array

#archivo de lectura
file="keylog.txt"
#a: <list> contador de cuantas veces existe ese numero en conjunto a
#b: <list> contador de cuantas veces existe ese numero en conjunto b
#c: <list> contador de cuantas veces existe ese numero en conjunto c
a=[0]*10
b=[0]*10
c=[0]*10
#sc: <list> subconjunto unico en c
sc=[]
#sa: <list> subconjunto unico en a
sa=[]
#borrar:<int> arreglo cual debe borrar
borrar=[]
#pathfinal:<int> orden final
pathfinal=[0]*10
#paso:<int> paso
paso=[False]*10

try:
    # abro el archivo y creo id de posiciones
    with open(file,"r+") as f:
        # recorro el archivo
        for text in f:
            i=0
            # recorro por caracter
            for mtext in text:
                #verifico que el caracter este en la lista de numeros
                if mtext != '\n':
                    #agrego a la lista para cada conjunto
                    if i==0:
                        a[int(mtext)]=a[int(mtext)]+1
                    if i==1:
                        b[int(mtext)]=b[int(mtext)]+1
                    if i==2:
                        c[int(mtext)]=c[int(mtext)]+1
                i=i+1
    #Los extremos : el que no tiene precentes y el no lo precede nadie
    for i in range(10):
        if(a[i]==0 and b[i]==0):
            sc.append(i)
        if(c[i]==0 and b[i]==0):
            sa.append(i)
    # Eliminar duplicados: signifca que no hay conexion con esos
    for i in range(len(sc)):
        if sc[i] in sa:
            sa.remove(sc[i])
            borrar.append(sc[i])
    for i in range(len(borrar)):
        if borrar[i] in sc:
            sc.remove(borrar[i])
    # Poner en matrix poner numero grande y mas pequeño
    pathfinal[sa[0]]=1
    pathfinal[sc[0]]=10
    # asignar columna como marcada
    paso[sa[0]]=True
    paso[sc[0]]=True

    #arreglo : <list> matriz con todos los conjuntos
    arreglo=[]
    arreglo.append(a)
    arreglo.append(b)
    arreglo.append(c)
    #maxi : <list> agregar numeros de mayor a menor
    maxi=[]
    #grupo : <list> agregar el grupo del numeros
    grupo=[]
    #num : <list> agregar la posicion del numeros
    num=[]
    # Recorrer el las posicones faltantes
    # saber orden de cantidad de aparicion de numero, se almacena la posicion y a que subconjunto pertenece
    for t in range (8):
        max=0
        pos_grupo=0
        pos_numero=0
        for i in range(3):
            for j in range (10):
                if paso [j]==False and max<arreglo[i][j]:
                    max=arreglo[i][j]
                    pos_grupo=i
                    pos_numero=j

        maxi.append(max)
        grupo.append(pos_grupo)
        num.append(pos_numero)
        paso [pos_numero]=True
    #Asignacion de posicion, respecto a los pesos
    for i in range (len(maxi)-1):
        if grupo[i]==2:
            bandera=0
            for jj in range (10):
                if bandera==0 and 9-jj not in pathfinal and num[i]!=0:
                    pathfinal[num[i]]=9-jj
                    bandera=1
        if grupo[i]==0:
            bandera=0
            for jj in range (10):
                if bandera==0 and jj not in pathfinal and num[i]!=0:
                    pathfinal[num[i]]=jj
                    bandera=1
        if grupo[i]==1:
            bandera=0
            for jj in range (5):
                if a[num[i]]>c[num[i]] and bandera==0 and 5-jj-1 not in pathfinal and num[i]!=0:
                    pathfinal[num[i]]=5-jj-1
                    bandera=1
                if a[pos_numero]<c[pos_numero] and bandera==0 and 5+jj+1 not in pathfinal and num[i]!=0:
                    pathfinal[num[i]]=5+jj+1
                    bandera=1
                if a[pos_numero]==c[pos_numero] and bandera==0 and 5+jj not in pathfinal and num[i]!=0:
                    pathfinal[num[i]]=5+jj
                    paso [5+jj]=True
                    bandera=1

    #impre: <list> numero a imprimir
    impre=[]
    for i in range (len(pathfinal)):
        if pathfinal[i]==0:
            pathfinal[i]=99
    #Organizacion de la impresion
    for i in range (len(pathfinal)):
        mini=min(pathfinal)
        if mini!=99:
            inx=pathfinal.index(mini)
            pathfinal[inx]=99
            impre.append(inx)

    print("Clave optima")
    print(impre)

    f.close()
except FileNotFoundError:
    pass