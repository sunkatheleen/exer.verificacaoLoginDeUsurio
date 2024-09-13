loginUser = "login123"
senhaUser = "senha123"

login = input("Insira o seu login:")
senha = input("Insira sua senha:")

while (True):
    if login == loginUser and senha == senhaUser:
        print("Bem-vindo ao sistema!")
        break
    else:
        print("Dados incorretos, por favor digite as informações novamente.")
        login = input("Insira o seu login:")
        senha = input("Insira sua senha:")