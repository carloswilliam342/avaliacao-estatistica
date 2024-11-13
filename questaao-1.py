import matplotlib.pyplot as plt


intervalos = ["300-400", "400-500", "500-600", "600-700", "700-800", "800-900", "900-1000", "1000-1100", "1100-1200"]
frequencias = [14, 46, 58, 72, 86, 62, 38, 22, 6]

# ponto médio de cada intervalo
pontos_medios = [(int(intervalo.split('-')[0]) + int(intervalo.split('-')[1])) / 2 for intervalo in intervalos]

# Média
total_freq = sum(frequencias)
soma_ponderada = sum(ponto_medio * frequencia for ponto_medio, frequencia in zip(pontos_medios, frequencias))
media = soma_ponderada / total_freq

#  Mediana
# Expandindo os dados para uma lista completa com base nas frequências
dados_expandido = []
for ponto_medio, freq in zip(pontos_medios, frequencias):
    dados_expandido.extend([ponto_medio] * freq)

# Ordenando os dados
dados_expandido.sort()
n = len(dados_expandido)


if n % 2 == 0:
    mediana = (dados_expandido[n//2 - 1] + dados_expandido[n//2]) / 2
else:
    mediana = dados_expandido[n//2]

# Moda
contagem_frequencias = {}
for ponto_medio in dados_expandido:
    if ponto_medio in contagem_frequencias:
        contagem_frequencias[ponto_medio] += 1
    else:
        contagem_frequencias[ponto_medio] = 1

# ponto médio com a maior frequência
moda = max(contagem_frequencias, key=contagem_frequencias.get)

# Desvio Padrão

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


print("Média:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Desvio Padrão:", desvio_padrao)
print("Q1 (1º Quartil):", q1)
print("D3 (3º Decil):", d3)
print("D7 (7º Decil):", d7)
print("P15 (15º Percentil):", p15)
print("P90 (90º Percentil):", p90)

plt.bar(intervalos, frequencias, color='skyblue')
plt.xlabel("Intervalo de Área (m²)")
plt.ylabel("Número de Lotes")
plt.title("Distribuição de Frequência das Áreas dos Lotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()