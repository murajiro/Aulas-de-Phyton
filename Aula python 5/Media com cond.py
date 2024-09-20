cond = "s"
soma= 0
alunos = 0
while(cond=="s"):
    nome = input(f"Digite o nome do {alunos+1}° Aluno: \n")
    idade = int(input(f"Digite a idade do {alunos+ 1}° Aluno : \n"))
    soma = soma + idade
    alunos+=1
    cond = input("Deseja continuar a cadastrar os Alunos? 's' para sim e qualquer tecla para parar: ")
media= soma/alunos    
print(f"A media das idades dos {alunos} é igual a {media:.2f}!")    
