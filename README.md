Nomes: Lucas Mendes Israel, Gustavo Henrique Costa, Gabriel Kasten


OBS:
Caso necessário, rodar o comando 'pip install matplotlib' para instalar a biblioteca necessária para executar o código.

Para executar o código, basta digitar o comando 'python main.py' no terminal do projeto no VsCode, e inserir os dados solicitados/desejados para efetuar o cálculo e geração dos gráficos comparativos.


Descrição do Código:

Utilizamos a técnica de Swarm Intelligence (PSO) para otimizar os cálculos de lucro.

A função dijkstra é usada para calcular o caminho mais curto entre dois pontos em um grafo, dado um conjunto de conexões e seus respectivos custos. Esta função implementa o algoritmo de Dijkstra usando uma fila de prioridade (heap) para encontrar o menor custo de viagem entre dois nós.

Classe Particula: Representa uma partícula no contexto do PSO. Cada partícula é uma possível solução para o problema de roteamento.

Inicialização: A posição da partícula é uma permutação aleatória das entregas (sendo que cada entrega é uma tupla de (inicio, destino, bonus)).

Função calcular_lucro: Calcula o lucro total com base na ordem das entregas. O lucro é calculado considerando o tempo de viagem e o bônus associado a cada entrega. O tempo é ajustado usando o algoritmo de Dijkstra para calcular o custo de viagem.

Classe PSO: Implementa o algoritmo de Otimização por Enxame de Partículas.

Inicialização: Cria um conjunto de partículas e calcula a melhor posição global com base no lucro obtido.

Função otimizar: Executa o processo de otimização por um número máximo de iterações. Atualiza as melhores posições das partículas e a melhor solução global com base no lucro.

Aspectos da lógica PSO que utilizamos:

Representação da Solução: Cada partícula representa uma solução candidata, que é uma permutação das entregas. A posição da partícula é uma ordem possível de fazer as entregas.

Função de Avaliação: A função calcular_lucro avalia a qualidade de cada solução. Ela calcula o lucro total com base no tempo necessário para realizar todas as entregas e o bônus associado.

Atualização das Partículas: Em cada iteração, as partículas são avaliadas e, se uma partícula tem um lucro maior do que o melhor encontrado anteriormente, essa nova solução é armazenada como a melhor solução da partícula.

Melhor Solução Global: O algoritmo mantém a melhor solução global encontrada por qualquer partícula e atualiza conforme as partículas são ajustadas.
