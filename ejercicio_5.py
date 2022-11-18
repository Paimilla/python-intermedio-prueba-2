def imprimir_colores(**kwargs):
    for key, value in kwargs.items():
        print(key, value.upper())

def main():
    colores = {}
    while True:
        color = input("Ingrese un color favorito: ")
        if color == "salir":
            break
        else:
            colores[color] = color
    imprimir_colores(**colores)

if __name__ == '__main__':
    main()









