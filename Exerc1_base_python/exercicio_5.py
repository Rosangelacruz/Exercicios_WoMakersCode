# 5. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso
# de avião, carro e ônibus. Levando em consideração:
# ● avião = 600 km/h
# ● carro = 100 km/h
# ● ônibus = 80 km/h

def calcular_tempo_viagem(distancia, velocidade):
    return distancia / velocidade

def main():
    try:
        distancia = float(input("Digite a distância do percurso em km: "))

        if distancia <= 0:
            print("A distância deve ser maior que zero.")
            return

        velocidade_aviao = 600  # km/h
        velocidade_carro = 100  # km/h
        velocidade_onibus = 80  # km/h

        tempo_aviao = calcular_tempo_viagem(distancia, velocidade_aviao)
        tempo_carro = calcular_tempo_viagem(distancia, velocidade_carro)
        tempo_onibus = calcular_tempo_viagem(distancia, velocidade_onibus)

        print(f"\nTempo de viagem para {distancia} km:")
        print(f"Avião: {tempo_aviao:.2f} horas")
        print(f"Carro: {tempo_carro:.2f} horas")
        print(f"Ônibus: {tempo_onibus:.2f} horas")

    except ValueError:
        print("Por favor, insira um número válido para a distância.")

if __name__ == "__main__":
    main()
