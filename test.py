""" 
### 9.**Generazione random di storie**

Usando la lista qui sotto, estrai casualmente **5 parole con reinserimento** (cioè, i duplicati sono ammessi).  

Successivamente, inserisci casualmente queste parole negli spazi vuoti (indicati con "_") nella seguente frase:

*"In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico __ che proteggeva. Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto abbondante e le offrì il __ come dono, i suoi occhi si spalancarono e lei esclamò una sola parola, "__".  
Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un __.  
Nel 101° giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla donna saggia per donarglielo.  
Con un sorriso da un orecchio all’altro, e cantando canti di festa, la donna saggia guardò i suoi compaesani e disse: "Ora è giunto il tempo del banchetto - nessuno rimarrà mai più senza _!" Ci fu grande gioia e celebrazione."*


 """
 
import numpy as np
lista_parole = [
    'INSEDIAMENTO', 'SEPARAZIONE', 'DIFFERENZA', 'APPLICAZIONE', 'ATTEGGIAMENTO', 'VERDURA', 'IMPERO', 'RICEVIMENTO',
    'IGNORANZA', 'BIOGRAFIA', 'VISIONE', 'AGENTE DI POLIZIA', 'PROVA', 'PRESTAZIONE', 'PRESENTAZIONE', 'PARENTE',
    'GIUSTIFICAZIONE', 'FILOSOFIA', 'DIREZIONE', 'BENEFICIARIO', 'BATTERIA', 'CERIMONIA', 'AGONIA', 'RECUPERO',
    'ALFABETIZZAZIONE', 'CONSEGNA', 'SERBATOIO', 'VOLONTARIO', 'DEPOSITO', 'BIRILLO DA BOWLING', 'NEMICO', 'ANNUNCIO',
    'CARAMELLA ZUCCHERATA', 'FULMINE', 'PALLONCINO', 'COPERTA', 'SCOPERTA', 'PENALITÀ', 'GENERALE', 'ALPACA',
    'VANTAGGIO', 'HOT DOG', 'ABITO', 'MATEMATICA', 'VARIANTE'
]

# Estrazione casuale di 5 parole con reinserimento
parole = np.random.choice(lista_parole, 5)
print(parole)

testo = """In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico __ che proteggeva. Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto abbondante e le offrì il __ come dono, i suoi occhi si spalancarono e lei esclamò una sola parola, "__".  
Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un __.  
Nel 101° giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla donna saggia per donarglielo.  
Con un sorriso da un orecchio all’altro, e cantando canti di festa, la donna saggia guardò i suoi compaesani e disse: "Ora è giunto il tempo del banchetto - nessuno rimarrà mai più senza _!" Ci fu grande gioia e celebrazione."""
index = 0
while "_" in testo and index < len(parole):
    # Sostituisce la prima occorrenza di "_" con la parola corrente
    testo = testo.replace("_", parole[index], 1)
    index += 1
    
print(testo)