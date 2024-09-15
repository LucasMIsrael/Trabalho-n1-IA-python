from versao_basica import calcular_lucro_basico
from versao_otimizada import PSO
import time
import matplotlib.pyplot as plt

def ler_conexoes_usuario():
    num_conexoes = int(input("Quantas conexões deseja inserir? "))
    conexoes = {}

    for _ in range(num_conexoes):
        origem = input("Origem da conexão: ")
        destino = input("Destino da conexão: ")
        tempo = int(input(f"Tempo entre {origem} e {destino}: "))

        if origem not in conexoes:
            conexoes[origem] = {}
        conexoes[origem][destino] = tempo

        if destino not in conexoes:
            conexoes[destino] = {}
        conexoes[destino][origem] = tempo

    return conexoes

def ler_entregas_usuario():
    num_entregas = int(input("Quantas entregas deseja inserir? "))
    entregas = []

    for _ in range(num_entregas):
        inicio = int(input("Tempo de início da entrega: "))
        destino = input("Destino da entrega: ")
        bonus = int(input(f"Bônus para a entrega no destino {destino}: "))
        entregas.append((inicio, destino, bonus))

    return entregas

def executar_com_dados(conexoes, entregas):
    print("\nExecutando versão básica...")
    
    #versão básica
    inicio_tempo_basico = time.time()
    lucro_basico = calcular_lucro_basico(conexoes, entregas)
    tempo_execucao_basico = time.time() - inicio_tempo_basico
    print(f"Lucro básico: {lucro_basico}, Tempo de execução: {tempo_execucao_basico:.4f} segundos")

    print("\nExecutando versão otimizada...")
    #versão otimizada
    inicio_tempo_otimizado = time.time()
    pso = PSO(num_particulas=30, entregas=entregas, conexoes=conexoes, max_iter=100)
    lucro_otimizado = pso.otimizar()
    tempo_execucao_otimizado = time.time() - inicio_tempo_otimizado
    print(f"Lucro otimizado: {lucro_otimizado}, Tempo de execução: {tempo_execucao_otimizado:.4f} segundos")

    return (lucro_basico, lucro_otimizado), (tempo_execucao_basico, tempo_execucao_otimizado)

def plotar_graficos(resultados, tempos):
    lucro_basico, lucro_otimizado = resultados
    tempo_basico, tempo_otimizado = tempos

    #grafico de lucro
    plt.figure()
    plt.bar(['Versão Básica', 'Versão Otimizada'], [lucro_basico, lucro_otimizado], color=['blue', 'green'])
    plt.title('Comparação de Lucro')
    plt.ylabel('Lucro')
    for i, v in enumerate([lucro_basico, lucro_otimizado]):
        plt.text(i, v + 0.5, str(v), ha='center')
    plt.show()

    #grafico de tempo de execução
    plt.figure()
    plt.bar(['Versão Básica', 'Versão Otimizada'], [tempo_basico, tempo_otimizado], color=['blue', 'green'])
    plt.title('Comparação de Tempo de Execução')
    plt.ylabel('Tempo (segundos)')
    for i, v in enumerate([tempo_basico, tempo_otimizado]):
        plt.text(i, v + 0.01, f'{v:.4f}', ha='center')
    plt.show()

def main():
    print("Inserir dados das conexões:")
    conexoes = ler_conexoes_usuario()

    print("\nInserir dados das entregas:")
    entregas = ler_entregas_usuario()

    print("\nCalculando os lucros e tempos de execução...")
    resultados, tempos = executar_com_dados(conexoes, entregas)

    print("\nGerando gráficos...")
    plotar_graficos(resultados, tempos)

if __name__ == "__main__":
    main()
