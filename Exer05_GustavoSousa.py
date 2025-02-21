# Crie uma variável chamada “adivinha” e defina o valor como 50. 
# Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”
# diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
# Se ele inserir o mesmo valor que “adivinha”
# exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".

ad = 4
i =0
total = 0
while i in range(50):
    n1 = int(input("tente adivinhar o numero : "))
    if n1 != "4":
        total += 1
    else:
        break
print (total)
