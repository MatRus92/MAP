import re

regex_mail = "[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,}"
regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{0,18}$"

def check_mail(email):
    if re.fullmatch(regex_mail, email):
        print("Mail" + mail + " jest poprawny")
    else:
        print("Mail" + mail + " jest błędny")


def check_password(pwd):
    if re.fullmatch(regex_password, pwd):
        print("Hasło" + pwd + " jest poprawne")
    else:
        print("Hasło" + pwd + " jest błędne")


if __name__ == '__main__':
    mail = "test@gmail.com"
    check_mail(mail)

    mail = "kontakt@mateuszrus.pl"
    check_mail(mail)

    mail = "test.test.pl"
    check_mail(mail)

    print('-----------------------------')

    password = "test"
    check_password(password)

    password = "Pass1234"
    check_password(password)

    password = "P@SsW0rD432#"
    check_password(password)