# Exercício 3 - Cálculo da média

notas = []

for i in range(3):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")

if media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")
