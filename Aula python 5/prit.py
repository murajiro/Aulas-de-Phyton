n=int(input("quantos números você quer? \n"))
soma=0
for i in range(1,n+1):
    num=int(input(f"digite o valor do {i} número: \n"))
    soma+=num
print(f"a soma dos {n} números digitados é: {soma}")
