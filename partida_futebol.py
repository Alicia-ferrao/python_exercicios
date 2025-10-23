equipa1 = int(input("Digite os golos do Sporting: "))
equipa2 = int(input("Digite os golos do Benfica : "))


diferenca_golos = equipa1 - equipa2

print("Diferença : {}" .format(diferenca_golos))

if diferenca_golos == 0 :
    print("Empate")
elif diferenca_golos in [1,2,3,4]:
    print("Partida normal")
else:
    print("Goleada")
    
print("Fim.")