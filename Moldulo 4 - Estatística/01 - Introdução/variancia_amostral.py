import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

populacao = np.random.random(10000) * 1000
variancia_populacional = populacao.var()

numero_de_amostragens = 5

def calc_var(amostra, den):
  media = amostra.mean()
  var = ((amostra - media)**2 / (len(amostra) - den)).sum()

  return var

for den in range(3):
  variancias = []
  for n in range(100, 4001):
    variancia_amostral_media = 0
    for i in range(numero_de_amostragens):
      amostra = np.random.choice(populacao, size=n, replace=False)
      variancia_amostral = calc_var(amostra, den)
      variancia_amostral_media += variancia_amostral

    variancia_amostral_media /= numero_de_amostragens

    variancias.append([n, variancia_amostral_media])

  variancias_amostrais = pd.DataFrame(variancias, columns=['n', 'var'])

  plt.subplot(3, 1, den + 1)
  plt.title(f'Dividindo por n - {den}')
  sns.histplot(x=variancias_amostrais['var'], bins=200)
  plt.vlines(variancia_populacional, 0, 200, color='green', linestyle='--', label='Variância Populacional')
  plt.vlines(variancias_amostrais['var'].mean(), 0, 200, color='red', linestyle='--', label='Variância amostral média')
  plt.legend(fontsize=14)
  
plt.tight_layout()
plt.show()