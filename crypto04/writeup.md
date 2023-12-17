# 5th HighSchools CTF Workshop - Udine 2023

## [crypto] LCG giocattolo

### Analisi preliminare

Il servizio è composto a livelli. Inoltre, ci fornisce il modo in cui vengono generati i valori.
In particolare, un dato valore è dato da un'equazione lineare modulare con argomento il valore precedente.
$$V_2 = aV_1 + b \mod{modulo}$$

### Livello 0

Il primo livello ci fornisce tutti e 3 i parametri `a`, `b`, `modulo`.
Ci fornisce il primo valore `V1` e ci chiede di trovare `V2`.

Applicando semplicemente l'equazione iniziale possiamo trovare $$V_2 = aV_1 + b \mod{modulo}$$
Validiamo il valore e passiamo al livello 1.

### Livello 1

Il secondo livello ci fornisce `a` ed `n`.
Ci fornisce due valori `V1` e `V2` e ci viene chiesto di trovare `V3`.
Per produrre il valore successivo dobbiamo trovare il valore del parametro `b`.

Sappiamo che $$V_2 = aV_1 + b \mod{modulo}$$ quindi $$V_2 - aV_1 = b \mod{modulo}$$
Una volta trovato `b`, calcoliamo `V3` come fatto al livello 0.

Validiamo il valore e passiamo al livello 2.

### Livello 2

Il terzo livello ci fornisce `b` ed `n`.
Ci fornisce due valori `V1` e `V2` e ci viene chiesto di trovare `V3`.
Per produrre il valore successivo dobbiamo trovare il valore del parametro `a`.

In questo caso bisognerebbe conoscere il concetto di inverso modulare, ma, dato che il servizio fornisce il tool per calcolare la divisione modulare, ci basta conoscere numeratore e denominatore della divisione.

Sappiamo che $$V_2 = aV_1 + b \mod{modulo}$$ quindi $$\frac{V_2 - b}{V_1} = a \mod{modulo}$$
La divisione può essere calcolata tramite il tool fornito dal servizio.

Una volta trovata `a`, calcoliamo `V3` come fatto al livello 0.
Validiamo il valore ed otteniamo la flag.

### La flag

`flag{s3mpl1c3_m4t3m4t1c4}`
