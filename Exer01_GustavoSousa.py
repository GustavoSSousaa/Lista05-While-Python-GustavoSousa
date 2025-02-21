#- Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela
# quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
i = 0
total = 0
while i in range(50):
    n1 = int(input("Digite o numero : "))
    total += n1
    if total >50:
        break
print (total)