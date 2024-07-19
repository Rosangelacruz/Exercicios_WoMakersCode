# 6. Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. 
# A palavra secreta será representada por espaços em branco, um para cada letra da palavra. 
# O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra.
# Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. 
# Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. 
# Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra 
# ou exceda o número máximo de tentativas. Dica: Você precisará importar uma blioteca para resolver esse exercício.

import random

# Lista de palavras possíveis para o jogo
palavras = ['python', 'programacao', 'jogo', 'computador']

# Escolhe uma palavra aleatoriamente da lista
palavra_secreta = random.choice(palavras)

# Lista para armazenar as letras adivinhadas
letras_adivinhadas = []

# Número de tentativas que o jogador tem
tentativas = 6

# Loop principal do jogo
while tentativas > 0:
    # Cria a palavra oculta com '_' para letras não adivinhadas
    palavra_oculta = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])
    print("Palavra:", palavra_oculta)
    
    # Pede ao jogador para adivinhar uma letra
    letra = input("\nAdivinhe uma letra: ").lower()

    # Verifica se a letra já foi adivinhada
    if letra in letras_adivinhadas:
        print("Você já tentou essa letra.")
    # Verifica se a letra está na palavra secreta
    elif letra in palavra_secreta:
        letras_adivinhadas.append(letra)
        print("Boa! A letra está na palavra.")
    else:
        letras_adivinhadas.append(letra)
        tentativas -= 1
        print("A letra não está na palavra. Tentativas restantes:", tentativas)

    # Verifica se todas as letras da palavra secreta foram adivinhadas
    if all(letra in letras_adivinhadas for letra in palavra_secreta):
        print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
        break
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
