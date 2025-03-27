""" 
### **6. Valori di Co2**

1. Carica tramite numpy il file generato e salvato a lezione sulle emissioni di CO2

2. Calcola quanti valori ci CO2 sono sopra la soglia di 18  tonnellate per anno ed il loro valore medio

3. Calcola la frazione totale di emissione sopra la soglia (somma totale sopra la soglia/somma totale)

 """
 
import numpy as np
file = np.genfromtxt("data.csv", delimiter=',', skip_header=1)
years = file[:,0]
years = np.unique(years)
print(years)
for year in years:
    #print(year)
    year_data = file[file[:,0] == year]
   
#print(year_data)
