from CalcError import *
x,y,z=symbols("x y z")
varx=var(x,100,10)
vary=var(y,100,10)
ecuacion=ec(z,(x*y)/(x+y))
varz=ecuacion.calcErr(varx,vary)
varz.ver()