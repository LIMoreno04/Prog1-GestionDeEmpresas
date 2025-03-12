from entities.sector import Sector
from entities.empleado import Empleado
from entities.funciones import *


class gestion_de_empresas:
    def __init__(self):
        self._sectores=[]                                                   #lista de sectores existentes
        self._empleados=[]                                                  #lista de empleados registrados
        self._estado=""                                                     #estado actual del menu principal (1-6)

    #getters
    @property
    def empleados(self):
        return self._empleados
    
    @property
    def sectores(self):
        return self._sectores
    
    @property
    def estado(self):
        return self._estado
    
    
    #la unica cosa que intrinsicamente cambiaria constantemente es la variable del menu principal
    @estado.setter
    def estado(self,nuevo_estado):
        self._estado=revision_de_variable(nuevo_estado,0,6)

    def agregar_empleado(self,nuevo_empleado):
        if isinstance(nuevo_empleado,Empleado):                                 #solo permito agregar objetos de clase "Empleado" a la lista
            self._empleados.append(nuevo_empleado)
        else:                                                                   #igualmente en todo el programa, nunca aplico este metodo en nada que pueda no ser clase "Empleado"
            print("Empleado invalido (este error no deberia saltar)")           #por eso es que, en teoria, este texto no deberia tener forma de saltar (a noser que se fuerce llamandolo manualmente)

    def agregar_sector(self,nuevo_sector):  
        if isinstance(nuevo_sector,Sector):                                     #misma historia que para agregar_empleado
            self._sectores.append(nuevo_sector)
        else:
            print("Sector invalido (este error no deberia saltar)")             

    def Alta_de_empleado(self):
                nombre=input("Ingrese nombre del empleado:\n")
                while nombre=="":                                               #se piden y se verifica que los atributos dados sean validos (nombre no vacio, cedula numerica de 8 digitos, salario numerico positivo)
                    print("El nombre del empleado no puede ser vacio")
                    nombre=input("Ingrese nombre del empleado:\n")

            
            
                cedula=input("Ingrese cedula del empleado:\n")
                while not (len(str(cedula))==8 and cedula.isnumeric()):
                    print("Cedula invalida. Debe digitar 8 numeros sin puntos ni guiones.")
                    cedula=input("Ingrese cedula del empleado:\n")
                for i in self.empleados:
                    if i.cedula==cedula:
                        print("Empleado",i.nombre,"ya esta registrado en el sistema.")
                        return False



                salario=input("ingrese salario del empleado:\n")
                while not salario.isnumeric():
                    print("El salario debe ser un numero entero positivo.")
                    salario=input("ingrese salario del empleado:\n")
                salario=int(salario)


                cargo=input("Seleccione cargo del empleado indicando el numero:\n 1. Jefe de sector\n 2. Team leader\n 3. Analista en sistemas\n 4. Desarrollador fullstack\n")
                while not (cargo=="1" or cargo=="2" or cargo=="3" or cargo=="4"):       #soy un poco tonto, pero sirve
                    print("Digite numero entre 1 y 4.")
                    cargo=input("Seleccione cargo del empleado indicando el numero:\n 1. Jefe de sector\n 2. Team leader\n 3. Analista en sistemas\n 4. Desarrollador fullstack\n")
                cargo=int(cargo)
            
                if cargo==1:
                   cargo="Jefe de sector"
                elif cargo==2:
                    cargo="Team Leader"
                elif cargo==3:
                    cargo="Analista en sistemas"
                elif cargo==4:
                    cargo="Desarrollador Full Stack"


                nuevo_empleado=Empleado(nombre,cedula,salario,cargo)                #se crea un objeto de clase "Empleado" con los atributos dados, y se agrega a la lista de empleados
                self.agregar_empleado(nuevo_empleado)
                print("Empleado registrado correctamente.")

    def Alta_de_sector(self,Nombre_del_sector):
                    for i in self.sectores:                                                               #se busca si ya existe un sector registrado con el mismo nombre
                        if i.nombre==Nombre_del_sector:
                            print("Sector ya registrado.")
                            return False
                        
                    nuevo_sector=Sector(Nombre_del_sector)                                          #se crea un objeto de clase "Sector" y se agrega a la lista de sectores
                    self.agregar_sector(nuevo_sector)
                    print("Sector registrado con exito.")




    def Contador_de_empleados(self,sector,cargo):
                contador=0      #por si se pide de un cargo en especifico
                #por si se pide de todos los cargos:
                j="No"  #jefe (o hay, o no hay)
                t=0     #team leaders
                an=0    #analistas
                d=0     #desarrolladores

                if cargo==1:
                    cargo="Jefe de sector"
                elif cargo==2:
                    cargo="Team Leader"                         #en caso de que me den un cargo especifico (nº 1-4)
                elif cargo==3:                                  #convierto el numero que me dan al cargo correspondiente para asi compararlo con el atributo de los empleados
                    cargo="Analista en sistemas"
                elif cargo==4:
                    cargo="Desarrollador Full Stack"            



                for empleado in self.sectores[int(sector)-1].empleados:
                    if cargo!=5:                     #si me pidieron un cargo en especifico
                        if cargo==empleado.cargo:    #sumo al contador cada vez que encuentro uno de dicho cargo
                            contador+=1      
                    
                    
                    elif cargo==5:                                          #si me pidieron de todos
                        if empleado.cargo=="Jefe de sector":
                            j="Si"
                        elif empleado.cargo=="Team Leader":
                            t+=1                                                #cada vez que coincide le sumo uno al respectivo contador (o cambio de "No" a "Si" en el jefe)
                        elif empleado.cargo=="Analista en sistemas":
                            an+=1
                        elif empleado.cargo=="Desarrollador Full Stack":
                            d+=1
                    
                sector=self.sectores[int(sector)-1].nombre                 #reasigno la variable "sector" al nombre del sector en vez de ser el indice del mismo en la lista de sectores
                                                                           #por pura comodidad, nada mas
            
                if cargo!=5:
                                
                    print("El sector",sector,"posee",contador, "empleados del tipo",cargo,".")  
            
                elif cargo==5:
                
                    print("Empleados del sector",sector,":\nJefe de sector: ",j,"\nTeam Leaders: ",t,"\nAnalistas en sistemas: ",an,"\nDesarrolladores Full Stack: ",d)
                                                                            #doy la informacion de forma bonita




    def Selector_de_sectores(self):                                         #como muchas veces me vi teniendo que pedirle al usuario que elija un sector despues de listarlos a todos, hice un metodo que me haga eso mismo para poder reusarla
            if len(self.sectores)==0:
                print("No hay sectores registrados.")
                return None
            else:
                print("Seleccione un sector indicando el numero:\n")
                for i in range(0,len(self.sectores)):
                    print(i+1,".",self.sectores[i].nombre,"\n")
                s=input()
                s=revision_de_variable(s,1,(len(self.sectores)))

                return s                                                    #bastante autoexplicativo creo yo






    def menu(self):
      
        while self.estado!=6:
            self.estado=(input("\nMenu Principal \n\nDigite el numero correspondiente (0-6): \n 0. Ver registro \n 1. Alta de empleado \n 2. Alta de sector \n 3. Asignar empleado a sector \n 4. Otorgar puntos a un sector \n 5. Realizar consultas \n 6. Cerrar programa \n\n"))


            if self.estado==1:
                self.Alta_de_empleado()

            
            elif self.estado==2:
                sector=input("Ingrese nombre del sector a registrar:\n")              #se pide el nombre de sector a registrar y se verifica que no sea vacio
                while sector=="":
                    print("El nombre del sector no puede ser vacio.")
                    sector=input("Ingrese nombre del sector a registrar:\n")
                self.Alta_de_sector(sector)                                                 #se crea el sector llamando al metodo respectivo
                
                
                y=input("¿Desea insertar un empleado al sector?\n1.Si\n2.No\n")             #se ofrece ingresar un empleado al sector por primera vez
                while y!="1" and y!="2": #verificar que se este digitando o '1' o '2'            
                    print("Digite '1' para Si, o de lo contrario '2' para No.")
                    y=input("¿Desea insertar un empleado al sector?\n1.Si\n2.No\n")
                while y=="1":
                    cedula=input("Ingrese cedula del empleado a insertar:\n")            #si se inserta un empleado al sector, se seguira ofreciendo la opcion hasta que el usuario digite "2"
                    for i in self.sectores:
                         if i.nombre==sector:
                            i.add_empleado(self.empleados,self.sectores,cedula)
                            y=input("¿Desea ingresar otro empleado?\n1.Si\n2.No\n")                 #al final del bucle se vuelve a sobreescribir "y", de esta manera si se digita 1 ("Si"), se vuelve al inicio y se repite nuevamente
                            while y!="1" and y!="2": #verificar que se este digitando o '1' o '2'
                                print("Digite '1' para Si, o de lo contrario '2' para No.")
                                y=input("¿Desea insertar otro empleado al sector?\n1.Si\n2.No\n")
                            break
                if y=="2":                              
                     pass

                     
            elif self.estado==3:
                
                s=self.Selector_de_sectores()              #se pide al usuario elegir un sector de la lista
                if s==None:
                    pass                #esto solo pasa si aun no existen sectores creados
                else:
                    cedula=input("Ingrese cedula del empleado a insertar:\n")
                    while not len(cedula)==8:
                        cedula=input("La cedula debe ser de 8 digitos.\n")
                    self.sectores[int(s)-1].add_empleado(self.empleados,self.sectores,cedula)          #se pide cedula y se inserta el empleado correspondiente en el sector seleccionado
                     #                  ^^^
                     #el '-1' es pq al listarlos de forma linda, empiezo en el '1' pero las listas en python
                     #empiezan en el '0', asi que la eleccion del usuario esta corrida 1 unidad del indice real


            elif self.estado==4:

                s=self.Selector_de_sectores()
                if s==None:             #misma de antes, se pide un sector al usuario, si da none es pq no hay sectores
                    pass
                else:
                    b=False                                                        #b me dice si fue posible agregar los puntos en el mes digitado
                    while not b:
                        mes=input("Ingrese el mes al que se quieren asignar los puntos (1-12):\n")
                        mes=revision_de_variable(mes,1,12)
                        puntos=input("Digite cantidad de puntos a agregar:\n")
                        while not puntos.isdigit():
                            puntos=input("Por favor digite un numero positivo.\n")
                        puntos=int(puntos)
                        b=self.sectores[s-1].add_puntos(puntos,mes)               #siendo que la funcion add_puntos devuelve un booleano que dice si salio bien o no
       #              no para hasta recibir un b=True (add_puntos existosa)


            elif self.estado==5:
                k=input(" 1. Determinar cantidad de empleados por cargo en cierto sector.\n 2. Ranking de puntos (anual o mensual).\n 3. Estimar aumento de salario para una persona en especifico del sector ganador.\n 4. Calcular suma de dinero extra a pagar a un sector si este resulta ganador.\n")
                k=revision_de_variable(k,1,4)
                if k==1:
                    s=self.Selector_de_sectores()
                    if s==None:
                        pass
                    else:
                        c=input("Seleccione un cargo indicando el numero:\n 1. Jefe de Sector\n 2. Team Leader\n 3. Analista\n 4. Desarrollador Full Stack\n 5. Todos\n")
                        c=revision_de_variable(c,1,5)
                        self.Contador_de_empleados(s,c)
                elif k==2:
                    m=input("Digite mes (1-12) para el cual desea ver el ranking de puntos. En caso de querer ver el ranking anual, digite 0.\n")
                    m=revision_de_variable(m,0,12)

                    if m!=0:
                        ranking=Listar_puntos_mes(self.sectores,m)

                        ranking=Ordenar_ranking(ranking)
                        Listar_ranking(ranking)                                 
        
        
                    elif m==0:                                                          #Aca el desafio esta en entender las funciones "Listar_puntos","Listar_ranking", y "Ordenar_ranking"
                        ranking=Listar_puntos_total(self.sectores)
                        ranking=Ordenar_ranking(ranking)
                        Listar_ranking(ranking)                    

                elif k==3:
                    ganador=Sector_ganador(self.sectores)
                    if len(ganador.empleados)==0:
                        print("El sector ganador no tiene empleados.")
                        pass
                    else:
                        ganador.aumento_salario_individual()

        
                elif k==4:
                    print("Seleccione un sector indicando el numero:")
                    for i in range(0,len(self.sectores)):
                         print(i+1,".",self.sectores[i].nombre)
                    sec=input()
                    sec=revision_de_variable(sec,1,(len(self.sectores)))
                    print("El aumento monetario total si el sector",self.sectores[sec-1].nombre,"resulta ganador es de: $",self.sectores[sec-1].aumento_salario_global())
                    
        
        
            elif self.estado==0:    
                #Opcion extra: Ver el estado actual de todos los sectores y empleados, desplegado de forma medianamente linda (o un intento de...)
                print("\n\nSECTORES:\n")
                for i in self.sectores:
                    print("Sector:                        "+i.nombre+"\n\n\nPuntos: ",i.puntos,"\n\n\n==============================================================================\n")
                    print("\nEMPLEADOS:\n\n------------------------------------------------------------------------------")
                    for j in i.empleados:
                         print("                             Nombre:",j.nombre,"\nCedula:",j.cedula,"\nCargo:",j.cargo,"\nSalario: $",j.salario,"\n------------------------------------------------------------------------------")
                    print("\n\n==============================================================================\n==============================================================================\n==============================================================================\n\n")
                print("\nEmpleados sin registrar en ningun sector:\n")
                for i in self.empleados:
                    a=True
                    for t in self.sectores:
                        if a:
                            for j in t.empleados:
                                if i.cedula==j.cedula:
                                    a=False
                                    break
                             
                        else:
                            break
                    if a:
                         print("Nombre:",i.nombre,"..........Cedula:",i.cedula,"..........Cargo:",i.cargo,"..........Salario: $",i.salario)



if __name__=="__main__":
    prueba=gestion_de_empresas()
    prueba.menu()