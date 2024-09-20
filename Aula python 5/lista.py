lista=[0]*10
soma=0
for i in range(10):
    lista[i]=int(input(f"digite o {i+1}° elementos : "))
    soma+= lista[i]
print("numero digitados são: ")
print(lista)
print(f"o somatorio é {soma}")
