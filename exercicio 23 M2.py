n1=int(input("Digite o 1° valor:"))
n2=int(input("Digite o 2° valor :"))
opcao=0
while opcao!= 5 :
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] fim do programa''')
    opcao=int(input("Digite sua opção:"))
    if opcao== 1 :
        soma=n1+n2
        print("O valor da soma de {} e {} foi {}".format(n1,n2,soma))
    elif opcao==2 :
        multiplicação=n1*n2
        print("O resultado da multiplicação de {} x {} é {}".format(n1,n2,multiplicação))
    elif opcao==3 :
        if n1>n2 :
            maior =n1
        else :
            maior=n2
        print("O maior número entre {} e {} é {}".format(n1,n2,maior))
    elif opcao==4:
        n1 = int(input("Digite um novo valor:"))
        n2 = int(input("Digite outro valor :"))
    elif opcao==5 :
        print("Fim do programa....")
    else:
        print("Dado inválido. Tente novamente")
print("Fim do programa. volte sempre")




