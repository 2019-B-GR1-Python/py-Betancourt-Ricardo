# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:30 2019

@author: Asus
"""

import pandas as pd

path = "C://Users//Asus//Documents//GitHub//py-Betancourt-Ricardo//03 - pandas//data//artwork_data.csv"
path_guardado_bin = "C://Users//Asus//Documents//GitHub//py-Betancourt-Ricardo//03 - pandas//data//artwork_data_completo.pickle"
df4 = pd.read_csv(
        path)

df4.to_pickle(path_guardado_bin)

primero = df4.loc[1035,'artist']
primero = df4.iloc[0]

