import pandas as pd
import requests

datapre = pd.read_csv('/Users/diego/Downloads/comisiones-vecinales.csv',sep =';', encoding = "latin")
datapre.drop('COORDINACIÃN TERRITORIAL', axis=1, inplace=True)
#newcols = {}
#datapre.rename(columns=newcols, inplace=True)

print(datapre)
