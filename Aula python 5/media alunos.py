n=int(input(f"Digite a quantidade de alunos: "))
soma= 0

for i in range(1, n+1):
    nome= input(f"Digite o nome do {i}° aluno: ")
    idade= int(input(f"Digite a idade do {i}° aluno: "))
    soma+=idade
media= soma/n
print(f"A media de idade dos {n} alunos é de {media:.2f}")
                     
