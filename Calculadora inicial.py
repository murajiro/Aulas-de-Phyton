cont='sim'
#Condicional
while(cont=='sim'):
    a=int(input('Digite o primeiro valor: '))
    b=int(input('Digite o segundo valor: '))
    operador=input('Qual opereção você deseja fazer? soma(+) subtração(-) multiplicação(*)divisão(/): ')
    if(operador=='+'):
          print(f" O resultado é {a+b}")
    elif(operador=='-'):
        print(f"O resultado é {a-b}")
    elif(operador=='*'):
        print(f" O resultado é {a*b}")
    elif(operador=='/'):
        print(f" O resultado é {a/b} ")
    cont=input('Você quer realizar outra conta? ')
#Realizando as operações   
