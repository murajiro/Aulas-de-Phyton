alunos = int(input("Quantos alunos tem na turma: "))

while(alunos>=0):
    nome = input("Digite o nome completo do aluno: ")
    av1 = float(input("Digite a nota da av1 do aluno: "))
    av2 = float (input("Digite a nota da av2 do aluno: "))
    media = (av1 + av2)/ 2
    if(media>=6):
        print(f"O aluno {nome} ficou aprovado com média de {media:.2f}")
    elif(media>=4):
        print(f"O aluno {nome} ficou em prova final com média de {media:.2f}")
    else:
        print(f"O aluno {nome} ficou reprovado com média de {media:.2f}")
        
    print("-----------------------------")    
    alunos= alunos-1

