from entities.funciones import *


class Sector:
    def __init__(self,Nombre):
          self._nombre=Nombre
          self._empleados=[]                            #el atributo "lista de empleados" sera una lista con elementos objeto de clase "Empleado"
          self._puntos=[]                               #el atributo "puntos" sera una lista de listas del formato [puntos,mes], donde se almacenara cuantos puntos por mes tiene el sector
                                                        #ambos atributos son vacios al crearse el objeto
    @property
    def nombre(self):
          return self._nombre
    @property
    def empleados(self):
        return self._empleados
    @property
    def puntos(self):
          return self._puntos

    

    def list_empleados(self):

        for i in range(0,len(self._empleados)):
            print(i+1,".",self._empleados[i].nombre)
        
         
    
    def add_puntos(self,puntos,mes):
        if mes<1 or mes>12:                                                         #revisar que el mes dado es valido
               print("Mes invalido.")
               return False
          
        for i in self._puntos:                                                      #revisar si ya hay puntos registrados en el  mes dado
               if i[1]==mes:
                    i[0]+=puntos
                    print("Puntos agregados con exito.")
                    return True
        self._puntos.append([puntos,mes])                                      #si no se encuentra mes coincidente en la lista [puntos,mes], se agrega en un nuevo elemento de la lista
        print("Puntos agregados con exito.")
        return True
     

    def add_empleado(self,Empleados :list,Sectores :list,cedula):                  #funcion que va a insertar empleados en un sector
        for empleado in Empleados:                                                  #revisar que el empleado existe
            if empleado.cedula==cedula:
                for sector in Sectores:                                             #revisar que el empleado ya no se haya registrado en otro sector
                    for i in sector.empleados:
                        if i.cedula==cedula:
                            print("Empleado ya registrado en sector", sector.nombre)
                            return False
                if empleado.cargo=="Jefe de sector":                            #revisar que no hayan 2 jefes de sector
                     for i in self._empleados:
                          if i.cargo=="Jefe de sector":
                               print("Solo se permite un jefe por sector.")
                               return False
                

                self._empleados.append(empleado)
                print("Empleado agregado al sector", self._nombre, "con exito.")
                return True
        print("Empleado inexistente")     
        return False       
          
    
    
    
    def aumento_salario_individual(self):               #metodo que calcula el aumento del 15% a un empleado especifico del sector
        print("Seleccione empleado del sector",self._nombre,"al cual calcularle el aumento de salario (digitando el numero correspondiente):\n")    #se listan los empleados y se pide un input de 1-(cantidad de empleados del sector)
        self.list_empleados()
        empleado=input()
        empleado=revision_de_variable(empleado,1,(len(self.empleados)))
        print("Salario de",self.empleados[empleado-1].nombre,"luego del aumento: $",self._empleados[empleado-1].aumento_salarial())


    

    def aumento_salario_global(self):
         s=0
         for i in self.empleados:
              s+=i.salario*0.15             #devuelve el aumento de plata total luego de aumentarle en 15% el salario a todo el sector
         return s