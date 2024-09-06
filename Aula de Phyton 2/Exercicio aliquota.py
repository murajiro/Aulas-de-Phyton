nome= input("Digite o nome do cliente: ")
renda= float(input("Digite a renda do cliente: "))

if(renda<1903.98):
    aliquota = "Isento"
elif(renda<2826.65):
    aliquota = "7,5%"
elif(renda<3751.05):
    aliquota = "15%"
elif(renda<4664.68):
    aliquota = "22,5%"
else:
    aliquota = "27,5%"

if(aliquota=="27,5%"):
    print(f"{nome} com renda de {renda} foi papado pelo leão e vai pagar uma aliquota de: {aliquota}")
else:
    print(f"{nome} com renda de {renda} vai pagar uma aliquota de: {aliquota}")
    
