ano_atual = int(input("Digite o ano Atual : "))
ano_nasc = int(input("Digite o ano de nascimento : "))

idade = ano_atual - ano_nasc

print("O ano atual é {} e o ano de nascimento é {} A sua Idade é {} anos" .format(ano_atual,ano_nasc ,idade))

if idade >= 18 :
    print("Estás apto para conduzir.")
else:
    print("ATENÇÂO!!! Não apto para conduzir.")