import matplotlib.pyplot as plt


tempos = [
    61, 65, 43, 53, 55, 51, 58, 55, 59, 56,
    52, 53, 62, 49, 60, 50, 62, 63, 56, 55,
    53, 56, 55, 57, 64, 62, 54, 63, 54, 61,
    48, 54, 54, 71, 57, 53, 43, 48, 54, 48,
    57, 58, 44, 63, 49, 55, 52, 62, 52, 51
]

# Intervalo e amplitude para a tabela de frequências
intervalo_inicial = 40
intervalo_final = 75
amplitude = 5
intervalos = [(i, i + amplitude - 1) for i in range(intervalo_inicial, intervalo_final, amplitude)]

#  frequência de cada classe
frequencias = []
for intervalo in intervalos:
    frequencias.append(sum(1 for tempo in tempos if intervalo[0] <= tempo <= intervalo[1]))

#  ponto médio de cada intervalo
pontos_medios = [(intervalo[0] + intervalo[1]) / 2 for intervalo in intervalos]

# 1. Calcular Média
total_freq = sum(frequencias)
soma_ponderada = sum(ponto_medio * frequencia for ponto_medio, frequencia in zip(pontos_medios, frequencias))
media = soma_ponderada / total_freq

# 2. Calcular Mediana
# Expandindo os dados para uma lista completa com base nas frequências
dados_expandido = []
for ponto_medio, freq in zip(pontos_medios, frequencias):
    dados_expandido.extend([ponto_medio] * freq)

# Ordenando os dados
dados_expandido.sort()
n = len(dados_expandido)

#  mediana 
if n % 2 == 0:
    mediana = (dados_expandido[n//2 - 1] + dados_expandido[n//2]) / 2
else:
    mediana = dados_expandido[n//2]

#  Moda
contagem_frequencias = {}
for ponto_medio in dados_expandido:
    if ponto_medio in contagem_frequencias:
        contagem_frequencias[ponto_medio] += 1
    else:
        contagem_frequencias[ponto_medio] = 1

#  ponto médio com a maior frequência
moda = max(contagem_frequencias, key=contagem_frequencias.get)

# Desvio Padrão
# Variância = Soma((ponto_medio - media)^2 * frequencia) / total_freq
variancia = sum(((ponto_medio - media) ** 2) * frequencia for ponto_medio, frequencia in zip(pontos_medios, frequencias)) / total_freq
desvio_padrao = variancia ** 0.5

#  Quantis e Percentis
def calcular_percentil(dados, percentil):
    posicao = (len(dados) - 1) * (percentil / 100)
    base = int(posicao)
    resto = posicao - base
    if base + 1 < len(dados):
        return dados[base] + resto * (dados[base + 1] - dados[base])
    else:
        return dados[base]

q1 = calcular_percentil(dados_expandido, 25)
d3 = calcular_percentil(dados_expandido, 30)
d7 = calcular_percentil(dados_expandido, 70)
p15 = calcular_percentil(dados_expandido, 15)
p90 = calcular_percentil(dados_expandido, 90)

# Exibindo os resultados
print("Média:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Desvio Padrão:", desvio_padrao)
print("Q1 (1º Quartil):", q1)
print("D3 (3º Decil):", d3)
print("D7 (7º Decil):", d7)
print("P15 (15º Percentil):", p15)
print("P90 (90º Percentil):", p90)

intervalos_str = [f"{intervalo[0]}-{intervalo[1]}" for intervalo in intervalos]
plt.bar(intervalos_str, frequencias, color='skyblue')
plt.xlabel("Intervalo de Tempo (s)")
plt.ylabel("Frequência")
plt.title("Distribuição de Frequência dos Tempos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()