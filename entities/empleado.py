class Empleado:
    def __init__(self,Nombre,Cedula,Salario,Cargo):
        
        self._nombre=Nombre
        self._cedula=Cedula
        self._salario=Salario
        self._cargo=Cargo

                                                #getters
    @property
    def nombre(self):
        return self._nombre
    @property
    def cedula(self):
        return self._cedula
    @property    
    def salario(self):
        return self._salario
    @property
    def cargo(self):
        return self._cargo


    def aumento_salarial(self):
         return self.salario*1.15