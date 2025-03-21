""" ### **3. Seleziona il numero più vicino a 0.5 in un array casuale**
Genera un array 10 x 3 con numeri casuali nell'intervallo [0,1].
Per ogni riga, seleziona il numero più vicino a 0.5. Per farlo usa il fancy indexing. """

import numpy as np

a = np.random.rand(10,3)
print(a)
minValue = a[np.arange(10), np.argmin(np.abs(a - 0.5), axis=1)]
print(minValue)