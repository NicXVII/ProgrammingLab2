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
#print(years)
year_data = {}
for year in years:

    year_data[year] =  file[file[:,0] == year]
    #print(year, year_data)
   
countYear = {}
sumYear = {}
sumYearSotto = {}
print(len(year_data))
for year in year_data:
    countYear[year] = len(year_data[year][year_data[year][:,1] > 18])
    sum_val = np.sum(year_data[year][year_data[year][:,1] > 18, 1])
    #print(sum_val)
    sumYear[year] = sum_val / countYear[year] if countYear[year] > 0 else 0

    #print(year, countYear[year])

for year in sorted(countYear.keys()):
    print("Anno: ", year, "Emissioni sopra 18: ", countYear[year], "Media: ", sumYear[year])
    
sumTot = 0
for year in sumYear:
    sumTot += sumYear[year]


print("Somma totale sopra la soglia: ", sumTot)
print("Frazione totale sopra la soglia: ", sumTot / np.sum(file[file[:,1] >=0, 1]))