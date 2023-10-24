nome = input ("digite seu primeiro nome:")
sobrenome = input ("digite seu sobrenome:")
idade = int (input ("digite sua idade:"))

lista = list((nome, sobrenome, idade))

if idade >= 18:
    print ("Você é maior")
else:
    print ("você é menor")
    
print (lista)