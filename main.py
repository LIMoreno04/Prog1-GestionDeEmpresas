from entities.funciones import *
from entities.empleado import Empleado
from entities.sector import Sector
from gestion_de_empresas import gestion_de_empresas
if __name__=="__main__":
    Programa=gestion_de_empresas()
    pruebas=True
    if pruebas:
        Pepe=Empleado("Pepe","12345678",15000,"Desarrollador Full Stack")
        Rodolfo=Empleado("Rodolfo","22222222",18000,"Desarrollador Full Stack")
        JuanCarlos=Empleado("Juan Carlos","11111111",11700,"Analista en sistemas")
        Maria=Empleado("Maria","18273645",4000,"Analista en sistemas")
        Alfredo=Empleado("Alfredo","00000007",22000,"Team Leader")
        Willyrex=Empleado("Guillermo Diaz","00000013",250000,"Team Leader")
        Vegetta=Empleado("Samuel De Luque","77777777",7777777,"Jefe de sector")
        JulianCasablanca=Empleado("Julian Casablanca","00921277",500000,"Jefe de sector")
        Florencia=Empleado("Maria Florencia","09876543",38000,"Team Leader")
        Cristina=Empleado("Cristina","00000021",40000,"Team Leader")
        Adrian=Empleado("Adrian","00000105",50000,"Jefe de sector")

        Youtubers=Sector("Youtubers")
        Profes=Sector("Profes")
        Randoms=Sector("Randoms")
        a=Sector("a")
        b=Sector("b")
        c=Sector("c")
           
        Programa.agregar_empleado(Pepe)
        Programa.agregar_empleado(Rodolfo)    
        Programa.agregar_empleado(JuanCarlos)
        Programa.agregar_empleado(Maria)
        Programa.agregar_empleado(Alfredo)
        Programa.agregar_empleado(Willyrex)
        Programa.agregar_empleado(Vegetta)
        Programa.agregar_empleado(JulianCasablanca)
        Programa.agregar_empleado(Florencia)
        Programa.agregar_empleado(Cristina)
        Programa.agregar_empleado(Adrian)
    
        Programa.agregar_sector(Youtubers)
        Programa.agregar_sector(Profes)
        Programa.agregar_sector(Randoms)
        Programa.agregar_sector(a)
        Programa.agregar_sector(b)
        Programa.agregar_sector(c)


        Youtubers.add_empleado(Programa.empleados,Programa.sectores,"77777777")
        Youtubers.add_empleado(Programa.empleados,Programa.sectores,"00000013")
        Profes.add_empleado(Programa.empleados,Programa.sectores,"12345678")    
        Profes.add_empleado(Programa.empleados,Programa.sectores,"00000007")
        Profes.add_empleado(Programa.empleados,Programa.sectores,"00000105")
        Profes.add_empleado(Programa.empleados,Programa.sectores,"00000021")
        Profes.add_empleado(Programa.empleados,Programa.sectores,"09876543")
        Randoms.add_empleado(Programa.empleados,Programa.sectores,"11111111")
        Randoms.add_empleado(Programa.empleados,Programa.sectores,"22222222")
        Randoms.add_empleado(Programa.empleados,Programa.sectores,"18273645")
        Randoms.add_empleado(Programa.empleados,Programa.sectores,"00921277")
        
        Youtubers.add_puntos(1000,1)
        Randoms.add_puntos(1000,1)
        Profes.add_puntos(2000,1)
        Randoms.add_puntos(4000,1)
        Youtubers.add_puntos(4000,2)
        Profes.add_puntos(3000,10)
        a.add_puntos(3500,4)
        b.add_puntos(2000,4)
        c.add_puntos(3500,4)    
    Programa.menu()