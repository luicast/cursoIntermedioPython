def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def mensaje():
    msj = input("desea repetir el ejercicio[y/n]: ")
    if msj == "y":
        run()
    else:
        print("termino mi programa")

def run ():
    num = input("ingresa un numero: ")
    assert num.isnumeric() and int(num) < 0, "debes ingresar un numero"
    print(divisor(int(num)))
    print("termino mi programa")
    mensaje()

if __name__ == "__main__":
    run()