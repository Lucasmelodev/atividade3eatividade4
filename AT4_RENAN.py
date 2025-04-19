# 1- Importe o módulo statistics e crie uma lista com 14 elementos em ordem crescente
import statistics

dados = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# 2- Calcule a média e a mediana usando o módulo completo
media1 = statistics.mean(dados)
mediana1 = statistics.median(dados)
print("Média 1:", media1)
print("Mediana 1:", mediana1)

# 3- Use um alias (apelido) para o módulo statistics e refaça os cálculos
import statistics as st

media2 = st.mean(dados)
mediana2 = st.median(dados)
print("Média 2:", media2)
print("Mediana 2:", mediana2)

# 4- Importe apenas as funções mean e median do módulo statistics e refaça os cálculos
from statistics import mean, median

media3 = mean(dados)
mediana3 = median(dados)
print("Média 3:", media3)
print("Mediana 3:", mediana3)

# 5- Importe todas as funções do módulo statistics e calcule novamente a média e a mediana
from statistics import *

media4 = mean(dados)
mediana4 = median(dados)
print("Média 4:", media4)
print("Mediana 4:", mediana4)
