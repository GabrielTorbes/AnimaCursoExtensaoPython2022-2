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