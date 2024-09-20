num= int(input("Digite um número para a tabuada: "))
print("*"*18)
print(f"Tabuada de {num}")
print("*"*18)
for i in range(11):
    print(f"{num} x {i} = {num*i}")
    
