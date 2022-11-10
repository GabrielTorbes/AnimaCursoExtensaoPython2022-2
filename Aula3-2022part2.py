#Criação de funções

preco= 1999.90

#Calcula 5% de imposto, guardar na varialvel imposto e exibir na tela

imposto= preco*0.05
print(imposto)

preco2= 100
imposto2= preco2*0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto


#Aqui é o uso... aqui é imposto a calcular...
preco= 299
imposto= calcular_imposto(preco)
print(imposto)

#Agora calcular imposto a alíquota agora é 7%
valores= [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
  print(f"O Imposto de {valor} é {calcular_imposto(valor)}")
