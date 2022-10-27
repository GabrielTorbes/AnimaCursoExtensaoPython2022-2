##Aula 1
# Meu primeiro projeto Python!!!
print("Hello World!!!")

nome = "Gabriel Torbes"
idade = 18
altura = 1.76

print(nome)

print("Olá meu none é "+nome)

#Tem que colocar o +str se nao for string
print("Olá minha idade é "+str(idade))
print("Olá minha altura é "+str(altura))

#Tem que colocar o f antes para formatar
print(f"Olá meu nome é {nome}, minha idade é {idade} e minha altura {altura}!!!")

#Tem que colocar o .format 
print("Minha idade é {} anos".format(idade))

#Quando quiser colocar duas variaves com .format
print("Meu nome é {} e eu tenho {} anos".format(nome,idade))

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
  print(f"Parábens {nome1}, Você é maior de idade, ótimo! Já pode beber e dirigir.")
   
else:
  
  print(f"Putz {nome1}, você ainda é novo demais para beber e dirigir.")

genero= input("Qual o seu Gênero Marculino = M / Feminino = F: ")

if (idade>= 17 and genero == "M"):
  print("Pelo visto você já fez o alistamento militar ou está fazendo.")

  


 
    

