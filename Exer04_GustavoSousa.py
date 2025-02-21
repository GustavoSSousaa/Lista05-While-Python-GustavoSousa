# Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Depois disso
# , exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
# Em seguida, pergunte se ele quer convidar outra pessoa.
# Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.
i=0
total = 0
nomes = []

while i in range(1):
    nome = str(input("Digite o nome do convidado : "))
    nomes.append(nome)

    des_con = str("Voce quer convidar ele pra festa s/n : ")

    des = str("Voce quer convidar mais alguem pra festa s/n : ")
    if des_con == "s":
        total += 1
    if des == "n":
        break
print (nomes)
print (total)

#erro na impressao das perguntas
