def CheckNumber(num):
    suma = 0
    for a in range(1, (int(num / 2) + 1)):
        if num % a == 0:
            suma += a

    if suma == num:
        return 'TAK'
    else:
        return 'NIE'


if __name__ == "__main__":
    print(CheckNumber(123))
    print(CheckNumber(28))
    print(CheckNumber(32))
    print(CheckNumber(6))

