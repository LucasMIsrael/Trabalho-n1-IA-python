def calcular_lucro_basico(conexoes, entregas):
    tempo_atual = 0
    lucro_total = 0
    for entrega in entregas:
        inicio, destino, bonus = entrega
        if tempo_atual <= inicio:
            if 'A' in conexoes and destino in conexoes['A']:
                tempo_atual += conexoes['A'][destino]
                lucro_total += bonus
                tempo_atual += conexoes['A'][destino]
            else:
                print(f"Conexão de 'A' para {destino} não encontrada.")
    return lucro_total
