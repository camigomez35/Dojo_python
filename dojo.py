class dojo:
    def __init__(self,x,y,s):
        self.menor=x
        self.mayor=y
        self.salto=s
        self.rango=range(menor,mayor,salto)

    def suma(self):
        resultado=0
        for i in self.rango:
            resultado+=i
        return resultado

print("Ingrese menor")
menor=int(input())

print("Ingrese mayor")
mayor=int(input())

print("Ingrese salgo")
salto=int(input())

#rango=range(menor,mayor)
#print("La suma es: ", suma(rango))

calcular=dojo(menor,mayor,salto)

print("La suma es: ", calcular.suma())
