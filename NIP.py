def validate_nip(nip_str):
    nip_str = nip_str.replace('-', '')

    if len(nip_str) != 10 or not nip_str.isdigit():
        return 'Nieprawidłowy'

    digits = [int(i) for i in nip_str]
    weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    check_sum = sum(d * w for d, w in zip(digits, weights)) % 11


    if check_sum == digits[9]:
        return 'Prawidłowy'

    return 'Nieprawidłowy'


if __name__ == "__main__":
    print(validate_nip('7962943949'))
    #print(validate_nip('1234567890'))
    #print(validate_nip('796-294-39-49'))

