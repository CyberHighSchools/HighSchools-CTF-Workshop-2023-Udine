from scapy.all import *

capture = rdpcap("../attachments/dominio_non_sospetto.pcap")
with open("../flags.txt") as f:
    flag = f.read().strip()

exfil_data = []
for packet in capture:
    if packet.haslayer(DNSQR) and b"snakectf.org" in packet[DNSQR].qname:
        exfil_data.append(packet[DNSQR].qname[: -len(b".snakectf.org") - 1].split(b"-"))

exfil_flag = [""] * len(exfil_data)

for pos, char in exfil_data:
    exfil_flag[int(pos)] = char.decode()

exfil_flag = "".join(exfil_flag)
print(exfil_flag)

assert exfil_flag == flag
