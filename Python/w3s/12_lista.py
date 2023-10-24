#um por um usando for
cores = ["azul", "amarelo", "marrom", "roxo", "vermelho", "verde"]
for x in cores:
    print(x)
#ou usando o range() e len  
cores = ["azul", "amarelo", "marrom", "roxo", "vermelho", "verde"]
for i in range (len(cores)):
    print(cores[i])

#while    
cores = ["azul", "amarelo", "marrom", "roxo", "vermelho", "verde"]
i = 0 
while i < len (cores):
    print(cores[i])
    i = i + 1
