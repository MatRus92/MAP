def rol(text, num):
    return text[-num:] + text[:-num]


if __name__ == "__main__":
    print(rol('12345678', 2))
    print(rol('MateuszRus', 5))


