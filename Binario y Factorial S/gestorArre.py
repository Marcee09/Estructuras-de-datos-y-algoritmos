import numpy as np

class Pila:
    __numeros: np.ndarray
    __cantidad: int
    __tope: int

    def __init__(self,tope):
        self.__numeros = np.empty(tope, dtype=int)
        self.__cantidad = 0
        self.__tope = tope
    
    def insertar(self, numero):
        if self.__cantidad < self.__tope:
            self.__numeros[self.__cantidad] = numero
            self.__cantidad += 1
        else:
            print("No se pueden añadir más elementos al arreglo")
    
    def vacia(self):
        return self.__cantidad == 0
    
    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
            return None
        else:
            x = self.__numeros[self.__cantidad - 1]
            self.__cantidad -= 1  # Disminuimos la cantidad después de eliminar
            return x
    
    def mostrar(self):
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
            
            
            
        





            