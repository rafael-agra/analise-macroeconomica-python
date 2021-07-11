#Teste com o Pandas
import pandas as pd

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"

#Transforma o html em um dataframe do panda
dataframes = pd.read_html(url)


df = dataframes[0]

#Pega somente o dado da coluna Bank NameBank da linha 5
filtro = df["Bank NameBank"][5]

#Pega somente os dados das instituicoes que estao com o status `no acquirer`
dado_limpo = df[df["Acquiring InstitutionAI"] =="No Acquirer"]

print(dado_limpo)

#Cria uma planilha com os dados filtrados anteriormente
dado_limpo.to_excel("C:\\Users\\rafae\\OneDrive\\Documentos\\dados_filtrados.xlsx")