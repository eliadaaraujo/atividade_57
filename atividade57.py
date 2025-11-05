# Leia idades de várias pessoas até que o usuário digite -1.
# Calcule a média das idades somente dos maiores de 18 anos.
# Se não houver maiores de idade, exiba mensagem apropriada.

soma = 0
contador = 0

while True:
    idade = int(input("Digite uma idade (-1 para sair): "))
    if idade == -1:
        break
    if idade > 18:
        soma += idade
        contador += 1

if contador > 0:
    media = soma / contador
    print("Média das idades dos maiores de 18 anos:", media)
else:
    print("Nenhum maior de idade foi informado.")
