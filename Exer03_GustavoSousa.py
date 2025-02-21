# Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
# Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ n ".
# Depois que o loop for interrompido, exiba o total.
i = 0
total1 = 0
total =0

while i in range(50):
    n1 = int(input("Digite um numero : "))
    print ("")
    n2 = int(input("Digite um numero : "))
    print ("")
    total += n1 + n2
    des = str(input("Deseja continuar s/n : "))
    if des == "n":
        break
print (total)