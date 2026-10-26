nomesAprovados = ["João", "Maria", "Pedro", "Ana"]

nome = input("Digite seu nome: ").strip().lower()

if nome in [n.lower() for n in nomesAprovados]:
    print(f"{nome}: Aprovado!")
else:
    print(f"{nome}: Reprovado!")