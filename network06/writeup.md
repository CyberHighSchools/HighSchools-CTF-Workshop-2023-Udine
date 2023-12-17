# 5th HighSchools CTF Workshop - Udine 2023

## [network] Tartaruga as a Service

Questa challenge è pensata per insegnare a ottenere dati da catture di traffico tramite script.

## Soluzione

La cattura consiste di un semplice servizio API REST (3 azioni: solleva penna, abbassa penna, muovi avanti) che controlla una tartaruga robot. La flag è scritta in codice morse.

Un filtro interessante è `http and tcp.dstport == 5000` che mostra le richieste contenenti i comandi inviati al robot.

Questa challenge è eccessivamente lunga per essere risolta manualmente, quindi è necessario generare uno script per ottenere la flag.

## Script

### solve.py

```python
from morse import MORSE_CODE_DICT_REV
from scapy.all import *

capture = rdpcap("tartaruga.pcap")

# aggiungo una tabella per semplificare la traccia del robot
# se nel pacchetto trovo {"amount": 10} scrivo fwd10 nella traccia
# ...
trace_dict = {
    b'{"amount": 10}': "fwd10",
    b'{"amount": 30}': "fwd30",
    b'{"action": "down"}': "down",
    b'{"action": "up"}': "up",
}

# creo una variabile per la traccia del robot
trace = []
# per ogni pacchetto
for packet in capture:
    # controllo se il pacchetto è nel filtro
    if (
        packet.haslayer(TCP)
        and packet[TCP].dport == 5000
        and packet.haslayer(Raw)
        and packet[Raw].load.startswith(b"{")
    ):
        # e lo aggiungo in caso alla traccia
        trace.append(trace_dict[packet[Raw].load])

# unisco i vari pezzi della traccia
trace = "".join(trace)
# se ho [penna giù, avanti 10, penna su, avanti 10] mi sono mosso poco: punto
trace = trace.replace("downfwd10upfwd10", ".")
# se ho [penna giù, avanti 30, penna su, avanti 10] mi sono mosso tanto: linea
trace = trace.replace("downfwd30upfwd10", "-")
# se ho [penna su, avanti 30, penna giù] sto separando le lettere
trace = trace.replace("upfwd30down", " ")
# divido la traccia morse in singole lettere
trace = trace.split(" ")[:-1]

# infine trovo la flag
recovered_flag = "".join(MORSE_CODE_DICT_REV[c] for c in trace)
print(recovered_flag)
```

### morse.py

```python
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

MORSE_CODE_DICT_REV = {v: k for k, v in MORSE_CODE_DICT.items()} # Da morse a carattere
```
