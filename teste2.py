import pandas as pd
from matplotlib import pyplot as plt

'''
prices = pd.DataFrame({"Acao A": [10,12,14.3,15.5], "Acao B": [30,23.32,43.54,77]})

#calcula retorno
retorno = prices.pct_change()

print(retorno)

#mostra retorno num grafico
plt.plot(retorno)
plt.title('Taxa de Retorno')
plt.show()
plt.close()

'''
#Pega dados do .csv e substituir a coluna 0 pela coluna do arquivo
precos_ativos = pd.read_csv("C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\analise-macroeconomica-python\\ibovespa.csv", index_col= 0 )


precos_ativos.index = pd.to_datetime(precos_ativos.index, dayfirst= True)



print(precos_ativos.pct_change())