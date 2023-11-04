import pyshark



def log_to_file(message):
    with open('ourLog.log', 'a') as file:
        file.write(f'info: {message}\n')
def import_pcap(file):
    capture = pyshark.FileCapture(file)
    log_to_file("import_pcap read file")
    return capture


capture = import_pcap('Network.pcap')

# Iterate through packets
# for packet in capture:
#     print(packet)  # Prints out a summary of each packet

first_packet = capture[0]
first_packet_ip = capture[0].ip

print("\n____________________________\n", first_packet)
print("\n____________________________\n", first_packet_ip)

# wykrywanie ip które zapodaje sporo SYN
for packet in capture:
    if 'TCP' in packet and packet.tcp.flags_syn == '1' and packet.tcp.flags_ack == '0':
        print(f"Possible SYN Flood attack packet: {packet.ip.src} -> {packet.ip.dst}")
