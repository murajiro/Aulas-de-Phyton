pacientes = int(input("Insira o número de pacientes: "))
while(pacientes>0):
    nome = input("Digite o nome do Paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    altura = float(input("Digite a altura(em metros): "))
    peso = float(input("Digite o peso(em KG): "))
    imc= peso/(altura**2)

    if(imc <18.5):
        classificacao = "Abaixo do peso"
    elif(imc< 24.9):
        classificacao = "Peso regular"
    elif(imc < 29.9):
        classificacao = "Acima do peso"
    elif(imc < 34.9):
        classificacao = "Obesidade grau 1"
    elif(imc < 39.9):
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3 "
    print("----------------------------------------------------------")    
    print(f"Nome: {nome}\n idade: {idade} \n Altura : {altura:.2f} \n peso : {peso:.2f} \n IMC: {imc:.2f} --> {classificacao}"))    
    pacaientes= pacientes-1
    

    
    
