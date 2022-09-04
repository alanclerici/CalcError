from sympy import *
#-------inicio clase-----------
class var():
    #constructor
    def __init__(self,simbolo,data:float,error:float):
        self.dat=data
        self.err=error
        self.s=simbolo
    
    def ver(self):
        print(self.dat,"±",f"{format(self.err, '.4g')}%")
#-------fin clase-----------

#-------inicio clase-----------
class ec():
    #constructor
    def __init__(self,variable,ecuacion):
        self.v=variable
        self.e=ecuacion
    
    def ver(self):
        print(self.e)

    def calcErr(self,* variables):
        #ec: ecuacion de tipo ec, variables de tipo "var". Calula propagacion de errores
        #devuelvo objeto de tipo var construido con las variables locales "data" y "error"
        
        error=[]    #inicializa la lista vacia
        reemplazo=[]
        #genero el vector(reemplazo) para reemplazar var por valores en cada funcion
        for k in range(len(variables)):
            o_var=variables[k].s        #cargo el simbolo y el dato de cada variable
            o_data=variables[k].dat
            reemplazo.append([o_var,o_data])
        
        #calculo el valor de la funcion
        func=(self.e).subs(reemplazo)

        #i es la cantidad de derivadas parciales (cantidad de coordenadas de ec: x,y,z...)
        for i in range(len(variables)):
            o_var=variables[i].s        #cargo el simbolo y el dato de cada variable
            o_data=variables[i].dat 
            o_error=variables[i].err

            deriv=diff(self.e,o_var).subs(reemplazo) #calculo la derivada respecto de una variable

            #(o_error*o_data) es el error absoluto
            error.append(abs(deriv*(o_error*o_data)))

        #sumo los errores de cada coordenada y los divido por el valor de la func para obtener
        #el error relativo
        return var(self.v,float(func),float(sum(error)/func))
#-------fin clase-----------

'''
x,y,z=symbols("x y z")
varx=var(x,100,10)
vary=var(y,100,10)
ecuacion=ec(z,x*y)
varz=ecuacion.calcErr(varx,vary)
varz.ver()
'''