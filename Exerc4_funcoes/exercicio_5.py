# 5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro.
# Implemente a lógica para contar o número de vogais na stringe retorne o total de vogais. 
# Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

# Função para contar vogais
def contar_vogais(frase):
    # Lista de vogais
    vogais = "aeiouAEIOU"
    contador = 0
    
    # Contar vogais na frase
    for letra in frase:
        if letra in vogais:
            contador += 1
            
    return contador

# Solicita ao usuário para inserir uma frase
frase_usuario = input("Digite uma frase: ")

# Conta as vogais na frase
total_vogais = contar_vogais(frase_usuario)

# Exibe o resultado
print("O total de vogais na frase é:", total_vogais)
