from functools import reduce
def main():
    
    numeros = [2,3,4,5,6] 
    suma = reduce(lambda x, y: x + y, numeros)
    resta = reduce(lambda x, y: x - y, numeros)
    multiplicacion = reduce(lambda x, y: x * y, numeros)
    division = reduce(lambda x, y: x / y, numeros)
    exponente = reduce(lambda x, y: x ** y, numeros)
    raiz = reduce(lambda x, y: x ** (1/y), numeros)

    print("suma : ",suma, "\nresta : ",resta, "\nmultiplicacion : ",multiplicacion, "\ndivision : ",division, "\nexponente : ",exponente, "\nraiz : ", raiz)

if __name__ == '__main__':
    main()
