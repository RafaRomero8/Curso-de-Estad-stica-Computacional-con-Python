import sys

def fibonacci_recursivo(n):#n numero de fibonacci
    if n == 0 or n == 1:#si n es = 0 o n=1
        return 1 #regresa 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) #regeresa recursion de fibonacci
#ef
def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))#preguntar al usuario el numero
    resultado = fibonacci_dinamico(n)#resultado llamando a fibonacci recursivo
    print(resultado)