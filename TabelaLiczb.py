def tablica(rows, columns):
    elements = ''
    tab = []
    numerator = 0
    for i in range(int(rows)):
        for j in range(int(columns)):
            if numerator == 10:
                elements += '0 '
                numerator = 1
            else:
                elements += str(numerator) + ' '
                numerator += 1

        tab.append(elements)
        elements = ''
    for i in tab:
        print(i)


if __name__ == "__main__":
    tablica(5, 6)
    tablica(3, 3)


