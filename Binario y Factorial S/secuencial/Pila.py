import numpy as np

class Pila:
    def __init__(self, dimension):
        self.__numeros = np.empty(dimension, dtype=int)
        self.__cantidad = 0
        self.__tope = -1
    
    def insertar(self, numero):
        if self.__tope < len(self.__numeros) - 1:
            self.__tope += 1
            self.__numeros[self.__tope] = numero
            self.__cantidad += 1
            return numero
        else:
            print("Pila llena")
            return 0
    
    def vacia(self):
        return self.__tope == -1
    
    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return 0
        else:
            numero = self.__numeros[self.__tope]
            self.__tope -= 1
            self.__cantidad -= 1
            return numero
            
    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope + 1):
                print(self.__numeros[i])

            
    def mostrarBinario(self):
        binario = self.__numeros[:self.__cantidad].tolist()
        print(list(reversed(binario)))
    
    #Ejercicio 2: pasar numero decimal a binario
    def numABinario(self,num):
        numero=num
        while numero>0:
            residuo = numero % 2
            numero=numero//2
            self.insertar(residuo)
    
    #Ejercicio 3: escribir una funcion que simule el funcionamiento del stack de recursión,
    #durante la ejecución de la funcion factorial, que calcula factorial de un numero según:
    # n!= n*(n-1)! si n>0
    # n!= 1    si n=0
    
    def factorial(self,numero):
        print("Calculo de factorial de ",numero)
        if numero==0:
            factorial=1
            print(f"{numero}!={factorial}")
            self.insertar(numero)
        elif numero>0:
            factorial=1
            num=numero
            for num in range(numero, 0, -1):
                    self.insertar(num)
                    factorial*=(num)
                    num-=1
            print("Resultado final= ",factorial)
            
            
            
        





            