# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:45 2019

@author: Asus
"""

import pandas as pd

serie_artistas_repetidos = df4["artist"]

artistas = pd.unique(serie_artistas_repetidos)
artistas.size
len(artistas)

blake = df4["artist"] =='Blake, Robert'
blake.value.counts()

df_blake=df4[blake]