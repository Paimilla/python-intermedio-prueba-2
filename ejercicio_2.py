def primo(numero):
    for i in range(2, numero):
       if numero % i == 0:
            return False
    return True

def main():
    numeros_primos = list(filter(lambda x: primo(x), range(1, 1001)))
    print(numeros_primos)

if __name__ == '__main__':
    main()
