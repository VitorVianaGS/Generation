aluno = input("Digite o nome do aluno: ")
nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"{aluno}: Aprovado - Média: {media}")
elif media >= 5:
    print(f"{aluno}: Exame - Média: {media}")
else:
    print(f"{aluno}: Reprovado - Média: {media}")