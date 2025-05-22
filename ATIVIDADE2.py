# 2. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a
# coluna) do maior valor.


matriz = [
    [1,2,4,5],
    [1,2,5,8],
    [4,5,6,7],
    [1,2,3,9],
]
for linha in range(4):
    print(matriz[linha])
maior = matriz[0][0]
linham = 0
colunam = 0

for linha in range(4):
    for coluna in range(4):
        if coluna or linha:
            maior = matriz[linha][coluna]
            linham = linha
            colunam = coluna

print(f"O maior numero da sua matriz é {maior} na linha {linham} e coluna {colunam}!")
