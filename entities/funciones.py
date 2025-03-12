def revision_de_variable(var,a,b):          #funcion super util y recurrente que me dice si una variable dada como str es numerica y esta entre dos numeros dados, y entra en bucle hasta que se cumplan las condiciones, devolviendo un int que las cumple.
        nosirve=True
        while nosirve:
            while not var.isdigit():                #que el string sea numerico
                var=input("Por favor, digite un numero entero\n")
            if int(var)>=a and int(var)<=b:         #cuando es numerico, que los numeros cumplan las condiciones
                var=int(var)
                nosirve=False      #(sirve)
            else:
                print("Por favor, digite un numero entre",a,"y",b,"\n")
                var=input()
        return var












def Listar_puntos_mes(Sectores,mes):                                #Dado un mes, esta funcion devuelve una lista DESORDENADA de listas de la forma [nombre_del_sector, puntos_en_ese_mes] =================> En esencia una tabla con cada sector y sus respectivos puntos en el mes dado
        ranking=[]
        for sector in Sectores:                                     #se revisan todos los sectores
            Hayptsregistrados=False                                 #variable almacenando si el mes elegido tiene puntos
            for puntaje in sector.puntos:                           #se revisa en todas las listas [puntos,mes] del atributo "puntos" del sector elegido
                if mes==puntaje[1]:                                  #se verifica si el mes elegido coincide con alguno de los meses registrados en la lista de listas [puntos,mes] (atributo "puntos")
                    r=[sector.nombre,puntaje[0]]                    #si se encuentra, se crea una lista registrando los puntos del sector
                    ranking.append(r)
                    Hayptsregistrados=True                          #se usa la variable para registrar que el mes elegido tiene puntos
                    break
            if not Hayptsregistrados:                               #si la variable indica que no hay puntos en el mes elegido, es decir, no hubo coincidencia con el mes elegido en ninguna de las listas [puntos,mes],
                 r=[sector.nombre,0]                                #se crea una lista registrando que el sector tiene 0 puntos
                 ranking.append(r)                                  #en ambos casos (se hayan encontrado puntos o no), la lista con el registro de puntos se agrega a una lista del ranking, la cual de momento esta desordenada
        return ranking


def Listar_puntos_total(Sectores :list):                            #Lo mismo que la anterior, pero esta suma todos los puntos de todos los meses, y tmb escupe la lista de lsitas de forma [sector,puntos]
        ranking=[]
        
        for sector in Sectores:                                     #se pasa por todos los sectores
            p=0                                                     #variable a almacenar total de puntos
            for puntaje in sector.puntos:                           #pasando por todos los meses con puntos registrados
               p+=puntaje[0]                                        #se suman los puntos a la variable
            ranking.append([sector.nombre,p])                       #se agrega al ranking una lista registrando los puntos totales del sector
        return ranking






def Ordenar_ranking(ranking :list):                                 #Dada una lista de listas [nombre_sector, puntos], esta funcion la ordena de mas puntos a menos puntos

    for i in range(0,(len(ranking)-1)):                             #para cada sector "i" en la lista desordenada del ranking
        h=0                                                         #"h" variable que es 0 si el sector "i" no se mueve de lugar, y en caso de moverse a una posicion posterior, almacena dicha posicion 
        Se_mueve=True

        while Se_mueve:
            h=0

            for t in range(1,(len(ranking)-i)):                     #se compara la posicion de "i" con la de los sectores "t", que estrictamente vienen despues de "i" en la lista
                if ranking[i][1]<ranking[i+t][1]:                   #si se encuentra un sector "t" (posisionado despues) con mas puntos que "i"

                     h=i+t                                          #se guarda en la variable "h", de esta manera luego del bucle solo sobrevive el mayor "t"
            if h==0:

                 Se_mueve=False                                     #Si no se encontro un sector con mas puntos (posicionado posterior al "i"), se rompe el bucle while y se pasa al siguiente "i" (siguiente sector de la lista)
            else:                                                   #En caso contrario, significa que el sector debe moverse de posicion, y por tanto el sector "i+1" pasa a ser el "i", y por lo tanto no se debe probar con el siguiente "i", puesto que estariamos salteandonos el previo "i+1" (que ahora esta reindexado en "i"); y por esto nos mantenemos en el while
                ranking.insert(h+1,ranking[i])               
                ranking.remove(ranking[i])                          #se borra al sector "i" de su posición original y se coloca exactamente un lugar despues del mayor "t"

    return ranking
 #al repetir este bucle para todos los sectores "i", la lista queda ordenada de mayor a menor.




def Listar_ranking(ranking :list):                                  #Dado el ranking ya ordenado y lindo, esta funcion lo printea todo, pero de forma prolija Y CONTEMPLANDO HERMOSAMENTE A LOS EMPATES 
    h=0 
    for i in range(0,len(ranking)):
        if i>=h:
            h=0                                                                         #h sera la variable que almacena, en casos de empate, cual es el proximo elemento del ranking con el cual NO hay empate, y para no repetir el proceso en cada sector empatado, solo se avisará la primera vez que se detecte un empate
            empates=[[i,ranking[i][0]]]                                                 #matriz de empates con el sector "i" (que de momento solo tiene al mismo sector "i" puesto que, obviamente, todos los sectores "empatan" consigo mismos)
            for t in range(0,len(ranking)):                                             #se compara con todos los otros sectores de la lista (no con él mismo (creo que no afectaba en nada hacer que se compare consigo mismo y hacer que la matriz de empates empiece vacia, pero asi funciona asi que no lo toco xd))
                if t!=i:
                    if ranking[i][1]==ranking[t][1]:                                    #si tienen la misma cantidad de puntos
                        empates.append([t,ranking[t][0]])                               #el sector "t" se agrega a la lista de empates del "i", y asi con todos los sectores "t" del ranking
            if empates!=[[i,ranking[i][0]]]:                                            #si la lista de empates es DISTINTA de una lista con solo sí mismo, entonces debe tener mas elementos, es decir HAY ALGUN EMPATE
                for e in range(1,len(empates)):                                         #
                    if empates[e][0]==i+1:                                              #No voy a mentir, no tengo idea de pq puse estas 4 lineas acá. Según yo reescriben la lista de empates exactamente igual ?????
                        empates.insert(e,empates[0])                                    #
                        empates.remove(empates[0])                                      #No se, es tarde y estoy cansado, la vdd que, de vuelta, si asi funciona no me voy a poner a cambiar las cosas :)
                        break                                                           #
                texto="(empate)"
                for x in empates:
                      texto+=" "+str(x[0]+1)+"º"
                texto+=": "
                for x in empates:
                    texto+=str(x[1])+", "
                texto+="con "+str(ranking[i][1])+" puntos."
                print(texto)                                                            #escribo el empate que hubo
                h=i+len(empates)                                                        #como no quiero repetir este proceso para los t siguientes sectores con los cuales empató (puesto que repetiria que hubo el mismo empate "t" veces), almaceno en una variable cual deberia ser mi siguiente puesto del ranking en chequear
            
            else:                                                                       #en caso de que no hayan empates
                texto=str(i+1)+"º"
                texto+=": "+str(ranking[i][0])+" con "+str(ranking[i][1])+" puntos."    #se notifica el sector ganador :D       (good ending)
                print(texto)










def Sector_ganador(Sectores :list):                                 #Esta funcion recibe la lista de sectores y devuelve el sector con mas puntos. En caso de empate le da a elegir al usuario cual tomar como ganador.
    x=[]                                                            #x sera la lista final con todos los sectores ganadores (o el unico sector ganador si no hay empates), todos en modo de objeto de clase sector
    ranking=Listar_puntos_total(Sectores)
    ranking=Ordenar_ranking(ranking)   #(obtener ranking ordenado)
    sectores_ganadores=[]                                           #mientras que la lista sectores_ganadores sera de uso momentaneo y solo almacenaria los nombres de los sectores, no los objetos
    for i in ranking:
        if ranking[0][1]==i[1]:                                     #una vez recibido el ranking ordenado, simplemente se agregan a la lista todos los sectores
            sectores_ganadores.append(i[0])                         #con la misma cantidad de puntos que el sector en el primer puesto (usualmente solo seria el primero, pero esto cubre los casos de empates)
    
    
    for sector_ganador in sectores_ganadores:
        for sector in Sectores:
            if sector_ganador==sector.nombre:
                x.append(sector)                                    #luego se busca por el nombre a los sectores ganadores y se appendean los objetos sector a la lista x

    if len(x)==1:
        print("Sector ganador: ",x[0].nombre)
        return x[0]                                                 #si x tiene solo un elemento, ese es el ganador y listo
    else:                                                           #si no....
        texto="Hay un empate de primer lugar entre:\n"
        for i in range(0,len(x)):
            texto+=str(i+1)+". "+x[i].nombre+"\n"                                                   #se listan los sectores en x
        texto+="¿Que sector desea elegir como ganador? (digite el numero correspondiente)"          #y se da la opcion al usuario de elegir uno
        print(texto)
        a=input()
        a=revision_de_variable(a,1,len(x))
        print("Tomando sector", x[a-1].nombre,"como el ganador.")
        return x[a-1]                                                                               #se devuelve el sector seleccionado