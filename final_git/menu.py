from binarios import caracter_binario
from binarios import palabra_binario
from binarios import binario_palabra


def main():
    opcion = int(input("1. [cosa 1]\n2. [COSA2]\n3. [COSA3]\n"))
    if opcion == 1:
        a = input("Ingrese una caracter: ")
        binario = caracter_binario(a)
        print(binario)
    elif opcion == 2:
        a = input("Ingrese una palabra: ")
        binario = palabra_binario(a)
        print(binario)
    elif opcion == 3:
        a = input("Ingresa un binario: ")
        binario = binario_palabra(a)
        print (binario)


if -__name__ == "__main__":
    main()