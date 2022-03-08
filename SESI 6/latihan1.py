print("\n-----------------SESI 6-----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')

print(len(df))
print(df.shape)
pd.set_option("display.max.colums",3)
print(df.head(2))
print(df.info())
print(df.describe())