##Segunda Aula
##Quando quiser que o usuario digite o seu nome
nome1= input("Digite Seu Nome: ")

#Comando para exibir na tela
print(f"Prazer, seu nome é {nome1}")
##Para virar inteiro é só colocar o int() antes do input
idade1= int(input("Digite sua Idade: "))
altura1= input("Digite sua Altura: ")

print(f"Sua Idade é {idade1}")
print(f"Sua Altura é {altura1}")
##Outro jeito é colocar o int() antes da variante
soma= int(idade1) * 2
print(f"O dobro da sua idade é: {soma}")

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber e dirigir"
if (idade1 >= 18):
  print(f"Parábens {nome1}, Você é maior de idade, ótimo! Já pode beber e dirigir.")

else:
  print(f"Putz {nome1}, você ainda é novo demais para beber e dirigir.")
