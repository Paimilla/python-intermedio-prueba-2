pedro = [4,5,6,7,4,3]
juan = [5,6,4,3,3,3]
maria = [6,6,5,4,3,3]
promedio_notas = []

def main():
    promedio_notas = list(map(lambda x: (x[0] + x[1] + x[2]) / 3, zip(pedro, juan , maria))) 
    redondear = list(map(lambda x: round(x, 2), promedio_notas))
    print( redondear,"\n\nHistoria :", redondear[0] , "\nLenguaje :", redondear[1] , "\nMatematicas :", redondear[2] , "\nFisica :", redondear[3] , "\nQuimica :", redondear[4] , "\nBiologia :", redondear[5] , "")
    

if __name__ == '__main__':
    main()