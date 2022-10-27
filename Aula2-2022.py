##Segunda Aula
##Quando quiser que o usuario digite o seu nome
nome1= input("Digite Seu Nome: ")

#Comando para exibir na tela
print(f"Prazer, seu nome é {nome1}")
#Para virar inteiro é só colocar o int() antes do input
idade1= int(input("Digite sua Idade: "))
altura1= input("Digite sua Altura: ")

print(f"Sua Idade é {idade1}")
print(f"Sua Altura é {altura1}")
#Outro jeito é colocar o int() antes da variante
soma= int(idade1) * 2
print(f"O dobro da sua idade é: {soma}")

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber e dirigir"
if (idade1 >= 18):
  print(f"Parabéns {nome1}, Você é maior de idade, ótimo! Já pode beber e dirigir.")
   
else:
  
  print(f"Putz {nome1}, você ainda é novo demais para beber e dirigir.")

genero= input("Qual o seu Gênero Marculino = M / Feminino = F: ")

if (idade>= 17 and genero == "M"):
  print("Pelo visto você já fez o alistamento militar ou está fazendo.")

nota= float(input("Qual foi sua nota na prova: "))

if (nota == 10):
  print(f"Parábens {nome1} você é o bixão, mesmo hein doido")
elif (nota>=6 and nota <10):
  print("Parabéns você passou na prova!!!")
else:
  print("Burro, não passou")


numero = 1
print(numero)
numero = numero + 1
print(numero)
  