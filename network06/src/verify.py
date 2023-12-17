from morse import MORSE_CODE_DICT_REV
from scapy.all import *

capture = rdpcap("../attachments/tartaruga.pcap")
with open("../flags.txt") as f:
    flag = f.read().strip()

trace_dict = {
    b'{"amount": 10}': "fwd10",
    b'{"amount": 30}': "fwd30",
    b'{"action": "down"}': "down",
    b'{"action": "up"}': "up",
}
trace = []
for packet in capture:
    if (
        packet.haslayer(TCP)
        and packet[TCP].dport == 5000
        and packet.haslayer(Raw)
        and packet[Raw].load.startswith(b"{")
    ):
        trace.append(trace_dict[packet[Raw].load])

trace = "".join(trace)
trace = trace.replace("downfwd10upfwd10", ".")
trace = trace.replace("downfwd30upfwd10", "-")
trace = trace.replace("upfwd30down", " ")
trace = trace.split(" ")[:-1]

recovered_flag = "".join(MORSE_CODE_DICT_REV[c] for c in trace)
print(recovered_flag)

assert recovered_flag == flag
