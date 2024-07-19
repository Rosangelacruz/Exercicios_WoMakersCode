# 2. Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0

# Lista para armazenar as médias dos alunos
medias = []

# Loop para solicitar as notas de 5 alunos
for i in range(5):
    print(f"Aluno {i+1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1}: "))
        notas.append(nota)
    
    # Calcular a média das notas
    media = sum(notas) / len(notas)
    medias.append(media)

    # Exibir a média individual do aluno
    print(f"Média do Aluno {i+1}: {media:.2f}")

# Contar o número de alunos com média maior ou igual a 7.0
alunos_acima_7 = len([media for media in medias if media >= 7.0])

# Imprimir o número de alunos com média maior ou igual a 7.0
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_acima_7}")