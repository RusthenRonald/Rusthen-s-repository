primeiro=int(input("Digite o primeiro termo:"))
razao=int(input("Digite a razão:"))
c=1
termo=primeiro
total=0
mais=10
while mais!= 0 :
    total+=mais
    while c <= total :
        print(termo,end="-")
        termo+=razao
        c+=1
    print("pausa")
    mais=int(input("Quantos termos você quer  mmostrar a mais? :"))
print("fim")
