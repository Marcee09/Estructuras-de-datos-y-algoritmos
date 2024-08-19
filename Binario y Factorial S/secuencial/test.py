from Pila import Pila

def test():
    gestorArreglo = Pila(10)
    binario=Pila(10)
    factorial=Pila(10)
    
    gestorArreglo.insertar(10)
    gestorArreglo.insertar(20)
    gestorArreglo.insertar(30)
    gestorArreglo.mostrar()
    print("Elemento suprimido:", gestorArreglo.suprimir())
    gestorArreglo.mostrar()
    
    binario.numABinario(10)
    binario.mostrarBinario()
    
    factorial.factorial(5)
    factorial.mostrar()
    
    