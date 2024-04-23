"""
Número USP: 11801199
Curso: Engenharia de Computação
Semestre: 2024/1
Título: 0 - Tutorial Assignment

"""

# Importa a versão 3 da biblioteca imageio com o alias imageio
import imageio.v3 as imageio

filename = input().strip()

image = imageio.imread(filename)

# Solicita ao usuário que insira as coordenadas do pixel que deseja consultar na imagem
i = int(input().strip())
j = int(input().strip())

# Acessa o valor do pixel na posição (i, j) da imagem
pixel_value = image[i, j]

# Imprime o valor do pixel no formato RGB
print(pixel_value[0], pixel_value[1], pixel_value[2])
