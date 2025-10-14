n1 = int(input("Digite a primeira nota : "))
n2 = int(input("Digite a segunda nota : "))

media = float((n1 + n2)/2)

print("A sua média é de : {}" .format(media))
if media >= 10 :
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
