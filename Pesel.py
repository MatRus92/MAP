def check_pesel(pesel):
    if len(pesel) == 11:
        numb = int(pesel[0]) + (int(pesel[1]) * 3) + (int(pesel[2]) * 7) + (int(pesel[3]) * 9) + (int(pesel[4]))
        + (int(pesel[5]) * 3) + (int(pesel[6]) * 7) + (int(pesel[7]) * 9) + (int(pesel[8])) + (int(pesel[9]) * 3)
        + (int(pesel[10]))

        if numb % 10 == 0:
            return 'Poprawny'

    return 'Niepoprawny'


if __name__ == "__main__":
    print(check_pesel('11111'))
    print(check_pesel('12345678901'))
    print(check_pesel('62112861326'))
    print(check_pesel('62112861346'))

