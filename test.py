# ### **1.Consumo di alcol per paese** 
# Esegui un’**analisi esplorativa** focalizzata sul **consumo di alcol**.  
# Analizza i seguenti aspetti:
# * Visualizza i primi 10 paesi ordinati per total_litres_of_pure_alcohol (dal più alto)

# * Calcola la media del consumo di birra, vino, e distillati

# * Crea una nuova colonna alcohol_index che sia: `(beer_servings + wine_servings + spirit_servings) / 3`

# * Trova il paese con il valore massimo di alcohol_index

# * Filtra solo i paesi che consumano più di 100 birre all’anno

# Crea un bar chart dei 10 paesi con più consumo totale (total_litres_of_pure_alcohol)

# Crea un line plot con wine_servings ordinato per paese (usa sort_values)

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")
print(df)