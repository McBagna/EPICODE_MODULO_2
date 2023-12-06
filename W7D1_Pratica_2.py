import random

def pwdGenerator(scelta:int)->str:
    pwdSimple = ""
    pwdStrong = ""
    listaPwdSimple = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    listaPwdStrong = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!£$%&/()=?+*#"
    if scelta == 8:
        for i in range(8):
            pwdSimple += random.choice(list(listaPwdSimple))
        return pwdSimple
    elif scelta == 9:
        for i in range(20):
            pwdStrong += random.choice(list(listaPwdStrong))
        return pwdStrong


if __name__ == "__main__":
    scelta = int(input("Premi 8 per una password semplice, premi 9 per un password complessa \n"))
    pwd = pwdGenerator(scelta)
    print(pwd)
    