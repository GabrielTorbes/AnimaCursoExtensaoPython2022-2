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

#Declarar um função calcular_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a alíquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto= valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor,7)}")

  #se agora for 10%
  for valor in valores:
    print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor,10)}")
  