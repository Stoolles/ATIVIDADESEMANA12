# Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as
# seguintes informações sobre alunos de uma disciplina, sendo todas as
# informações do tipo inteiro:
# a. Primeira coluna: número de matrícula (use um inteiro)
# b. Segunda coluna: media das provas
# c. Terceira coluna: media dos trabalhos
# d. Quarta coluna: nota final
# Elabore um programa que:
# a. Leia as três primeiras informações de cada aluno;
# b. Calcule a nota final como sendo a soma da média das provas e da
# média dos trabalhos;
# c. Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe
# uma maior nota).


notas = [
    [1, 1, 5, 6],
    [2, 1, 5, 6],
    [3, 2, 5, 7],
    [4, 2, 5, 7],
    [5, 3, 5, 8],
]

for nota in notas:
    soma = nota[1] + nota[2]

maior_nota = notas[0][3]

matricula_maior_nota = notas[0][0]


