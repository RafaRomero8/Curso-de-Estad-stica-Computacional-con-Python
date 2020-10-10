import sys #imprtando la libreria sys

def fibonacci_recursivo(n):#n numero de fibonacci
    if n == 0 or n == 1:#si n es = 0 o n=1
        return 1 #regresa 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) #regeresa recursion de fibonacci

def fibonacci_dinamico(n, memo = {}):#recibe n parametro y recibe un diccionrio para le memorizacion
    if n == 0 or n == 1:
        return 1

    try:#mecanismo de control de flujo accede directamente al valor si n al except
        return memo[n] #llave n si la tenemos(regresa n)
    except KeyError:#si accedemos al diccionario y no esta la llave kyerror
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)#llamamos a fibonacci
        memo[n] = resultado
#guardamos los resutados en el diccionario
        return resultado

if __name__ == '__main__':
    sys.setrecursionlimit(10002)#define cual es el limite recursivo
    n = int(input('Escoge un numero: '))#preguntar al usuario el numero
    resultado = fibonacci_dinamico(n)#resultado llamando a fibonacci recursivo dinamico
    print(resultado)