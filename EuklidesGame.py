numberOfAttempts = input()

for x in range(0, int(numberOfAttempts)):

    ab = input()
    a = int(ab.split()[0])
    b = int(ab.split()[1])

    while True:
        if a == b or a == 0 or b == 0:
            break
        else:
            if a > b:
                a = a - b
            else:
                b = b - a

    print(a + b)


