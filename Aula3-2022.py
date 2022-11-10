print("Inicio da aula 3 dia (09/11/2022)")


contador = 1

# Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1



# Laço for (python for = for each)
fruta = "Morango"
print(fruta)

#Lista
frutas = ["Morango", "Laranja", "Bergamota"]

#Quero exibir apenas a 3a. fruta
print(frutas[2])

#Exibir quantas frutas tem na minha lista?
print(len(frutas))# length = tamanho

#Quero incluir uma fruta nova
frutas.append("Beterraba")

print(len(frutas))# length = tamanho
print(frutas)


print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])


print("Exemplo das fruas com while...")
i=0
while(i<len(frutas)):
  print(frutas[i])
  i= i + 1

print("Exemplo das frutas com FOR...")

for f in frutas:
  print(f)
