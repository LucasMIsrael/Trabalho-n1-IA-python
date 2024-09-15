import heapq
import random

def dijkstra(conexoes, origem, destino):
    dist = {nodo: float('inf') for nodo in conexoes.keys()}
    dist[origem] = 0
    pq = [(0, origem)]  
    
    while pq:
        (custo_atual, nodo_atual) = heapq.heappop(pq)
        
        if nodo_atual == destino:
            return custo_atual
        
        for vizinho, tempo in conexoes.get(nodo_atual, {}).items():
            custo = custo_atual + tempo
            if custo < dist[vizinho]:
                dist[vizinho] = custo
                heapq.heappush(pq, (custo, vizinho))
    
    return float('inf')  

class Particula:
    def __init__(self, entregas, conexoes):
        self.posicao = random.sample(entregas, len(entregas))
        self.velocidade = [0] * len(entregas)
        self.melhor_posicao = self.posicao[:]
        self.melhor_lucro = self.calcular_lucro(conexoes)
    
    def calcular_lucro(self, conexoes):
        tempo_atual = 0
        lucro_total = 0
        for entrega in self.posicao:
            inicio, destino, bonus = entrega
            if tempo_atual <= inicio:
                tempo_atual += dijkstra(conexoes, 'A', destino)  
                lucro_total += bonus
                tempo_atual += dijkstra(conexoes, destino, 'A')
        return lucro_total

class PSO:
    def __init__(self, num_particulas, entregas, conexoes, max_iter):
        self.particulas = [Particula(entregas, conexoes) for _ in range(num_particulas)]
        self.melhor_global = max(self.particulas, key=lambda p: p.melhor_lucro)
        self.max_iter = max_iter
        self.conexoes = conexoes

    def otimizar(self):
        for _ in range(self.max_iter):
            for particula in self.particulas:
                lucro_atual = particula.calcular_lucro(self.conexoes)
                if lucro_atual > particula.melhor_lucro:
                    particula.melhor_posicao = particula.posicao[:]
                    particula.melhor_lucro = lucro_atual
            self.melhor_global = max(self.particulas, key=lambda p: p.melhor_lucro)
        return self.melhor_global.melhor_lucro
