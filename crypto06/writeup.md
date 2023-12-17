# 5th HighSchools CTF Workshop - Udine 2023

## [crypto] L'ORACOLO DELLO XOR

### Analisi preliminare

Il servizio ci fornisce:

- la chiave privata cifrata con una chiave di sessione tramite lo XOR. Quindi, chiamata `SK` la chiave privata e `SESS` la chiave di sessione, quello che vediamo in codifica binaria nel cookie `Encrypted secret` è il risultato di $$SK \oplus SESS$$.
- la chiave pubblica `PK` calcolata con `SK`.

Il nostro obiettivo sarà quello di trovare `SK`. Per farlo dovremo prima trovare la chiave di session `SESS`.

Come indicato dal servizio, cambiando il valore del cookie (8 bit) e ricaricando la pagina, il servizio calcola la chiave privata `SK_primo` dal cookie inserito e genera la chiave pubblica associata che viene presentata sull'homepage.

### Come ottenere la chiave di sessione

1. Cosa succede se mettiamo `00000000` al posto del cookie originale? Il servizio calcolerà $$SK' = COOKIE \oplus SESS = SESS$$ e genererà la chiave pubblica associata alla chiave di sessione.

2. Cosa succede se mettiamo `00000001` al posto del cookie originale? Il servizio calcolerà la stessa chiave privata eccetto l'ultimo bit che potrà essere `1` o `0`. Se la chiave pubblica risultante fosse maggiore di quella ottenuta con il cookie tutto a zero, il primo bit della chiave di sessione sarebbe sicuramente `0` altrimenti sarebbe `1`. Questo è il motivo per cui il servizio offre un tool di comparazione.

#### Esempio: SESS = 01001101 - COOKIE0 = 00000000 - COOKIE1 = 00000001

Ipotizziamo che la chiave pubblica venga calcolata moltiplicando per 2 la chiave privata. Sappiamo, infatti, dal servizio, che la chiave pubblica e la chiave privata sono direttamente proporzionali.
$$V0 = SESS \oplus COOKIE0 = SESS = 01001101$$
$$V1 = SESS \oplus COOKIE1 = 01001100$$

$$P0 = V0 \times 2$$
$$P1 = V1 \times 2$$

Se `P1` > `P0` allora `SESS` avrà sicuramente uno `0` nel bit meno significativo, altrimenti avrà un `1`.
Nel nostro caso `P1` è minore di `P0` per cui `SESS` avrà un `1` come bit meno significativo. E possiamo notare, infatti, che `SESS = 01001101` il quale termina, appunto con `1`.

Questo si può fare per ogni bit, in particolare, al passo `3` il cookie sarà `00000010`, al passo `4` sarà `00000100` e così via.
In questo modo troveremo i vari bit della chiave di sessione `SESS`.

### Come ottenere la chiave segreta

Una volta trovata la chiave di sessione `SESS`, possiamo trovare `SK` calcolando lo xor tra il cookie originale e la chiave di sessione appena trovata.

Validiamo il valore segreto trovato per ottenere la flag.

### La flag

`flag{qu3st0_0r4c0l0_c1_d4_m0lti_sugg3r1m3nti}`
