# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import pandas as pd
from urllib.request import urlopen

def get_data_bcb(código):
    url = "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json".format(código)
    html = urlopen(url).read()
    df = pd.read_json(html)
    df.index = pd.to_datetime(df['data'])
    df = df['valor']
    return df

selic = get_data_bcb(11)
teste = get_data_bcb(300)


plt.plot(selic.index, selic)
plt.xlabel('Anos')
plt.ylabel('Taxa diária')
plt.title('Taxa Selic')
plt.show()
plt.close