def divisor(num):
    try:
        if num == 0:
            raise ValueError("ingresa un numero diferente de 0")
        elif num < 0:
            raise ValueError("ingresa un numero positivo")
        else:
            divisor = []
            for i in range(1, num + 1):
                if num % i == 0:
                    divisor.append(i)
        return divisor
    except ValueError as ve:
        print(ve)
        return False

def mensaje():
    msj = input(" desea repetir el ejercicio[y/n]: ")
    if msj == "y":
        run()
    else:
        print("termino mi programa")

def run ():
    try:
        num = int(input("ingresa un numero: "))
        print(divisor(num))
        print("termino mi programa")
        mensaje()
    except ValueError:
        print("deber ingresar un numero")
        mensaje()


if __name__ == "__main__":
    run()