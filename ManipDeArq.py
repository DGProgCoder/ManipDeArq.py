try:
    nome = str(input("\n \n=== Cadastro de Usuário === \n \nDigite o seu nome: "))
    email = (input("Digite o e-mail: "))
    idade = int(input("Digite a sua idade: "))
    idade2 = idade
    with open("bebereborn.txt", "a") as arquivo:
        arquivo.write(f"{nome}  |  {email}  |  {idade} \n")
    arquivo.close()
    
    if idade2 >= 18:
        print ("Maior de Idade")
    elif idade2 < 18:
        print ("Menor de Idade")

    while idade < 18:
        print ("Tente Novamente Abaixo: ")
        nome = str(input("Digite o seu nome: "))
        email = (input("Digite o e-mail: "))
        idade = int(input("Digite a sua idade: "))

        arquivo = open("bebereborn.txt", "a")
        arquivo.write(f"Nome:{nome}  |  E-mail:{email}  |  Idade:{idade} \n")
        arquivo.close()

    if idade >= 18:
        print (f"\n \n=== Dados Cadastrados === \nNome:{nome}  \nE-mail:{email} \nIdade:{idade} \nSituação:  \n \n \nDados salvos com sucesso no arquivo 'Cadastro.txt'.")

except:
    print ("Digite um número inteiro!")