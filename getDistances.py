import pandas as pd
import requests
import googlemaps
import numpy as np

API_key = 'Aqui poner tu API key'
gmaps = googlemaps.Client(key=API_key)

datapre = pd.read_csv('/Users/diego/Downloads/comisiones-vecinales.csv',sep =';', encoding = "latin")
datapre.drop('COORDINACIÃN TERRITORIAL', axis=1, inplace=True)
datapre.drop('LUGAR', axis=1, inplace=True)
datapre.drop('UBICACIÃN', axis=1, inplace=True)


# ============= API call =======================
n = len(datapre['geopoint'])
matriz = np.zeros((n+1,n+1))
for i in range(len(datapre['No.'])):
	matriz[i+1][0] = datapre['No.'][i]
	matriz[0][i+1] = datapre['No.'][i]
for i in range(n):
	for j in range(i):
		result = gmaps.distance_matrix(datapre['geopoint'][i], datapre['geopoint'][j])
		distancia = result['rows'][0]['elements'][0]['duration']['value']
		matriz[i+1][j+1] = distancia
pd.DataFrame(matriz).to_excel('matrizDist.xlsx', index=False, header=False)

