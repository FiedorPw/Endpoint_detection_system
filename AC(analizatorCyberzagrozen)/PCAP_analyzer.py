from import_file import log_to_file, import_pcap, analyze_pcap_packets
import os
from logger import Logger

#@click.argument('pcap_file', type=click.Path(exists=True))
#@click.option('--display_filter', help='BPF display filter for PCAP analysis')
def Pcap_analyzer(pcap_file, display_filter):

    Logger.output(f"Analyzing PCAP file: {pcap_file}")

    # Import PCAP file
    capture = import_pcap(pcap_file, display_filter)

    analyze_pcap_packets(capture)

def analyze_pcap_packets(capture):
    for packet in capture:
        print(packet)

def get_available_pcap_files(path):
    """
    Get the list of PCAP files in the specified path.
    """
    pcap_files = [file for file in os.listdir(path) if file.endswith('.pcap')]
    return pcap_files
def pcap_to_packet_array(pcap_file):
    packet_array = []
    for packet in pcap_file:
        packet_array.append(packet)
    # print("ilość pobranych pakietów do analizy: ",len(packet_array),"\n")
    return packet_array


def detectNetworkScanning(pcap_file):

    packet_array = pcap_to_packet_array(pcap_file)

    arpCount = 0
    arp_scan_detected = 0
    amount_arp_scan_detected = 0
    last_host = packet_array[0]

    for i in range(0,len(packet_array)):


        if  packet_array[i].highest_layer=='ARP':
            # senderIP = packet.
            arpCount += 1
            # print(f"ciąg arpów {arpCount}")
            if arpCount > 10 and arp_scan_detected == 0:
                amount_arp_scan_detected += 1
                print(f"prawdopodobne skanowanie sieci po raz {amount_arp_scan_detected}")
                arp_scan_detected = 1
        else:

            # print("nie poznaje")
            arpCount = 0
            arp_scan_detected = 0

    return f"sieć była skanowana {amount_arp_scan_detected} razy w pliku {pcap_file}\n", arp_scan_detected

def detectPortScanning(pcap_file):

    packet_array = pcap_to_packet_array(pcap_file)

    i = 0
    array_20packets = []
    rst_count = 0
    port_scaning_detected = 0
    detected_scans_amount = 0
    for i in range(0, len(packet_array)):

        #dodawanie do arraya który bedzie miał ,,okno" 20 pakietów z całego ruchu sieciowego na kolejce FIFO
        # i bedzie sprawdzał czy przynajmniej 8 z nich to były RST
        array_20packets.append(packet_array[i])

        if packet_array[i].highest_layer == 'TCP' and int(packet_array[i].tcp.flags_reset) == 1:
            # print("super tcp reset")
            rst_count += 1
        # usuwanie z tyłu kolejki
        if len(array_20packets) >= 21:
            if  array_20packets[0].highest_layer == 'TCP' and int(array_20packets[0].tcp.flags_reset) == 1:
                # print("wykopujemy rst")
                rst_count -= 1

            array_20packets.pop(0)
        if port_scaning_detected == 1 and rst_count < 5:
            port_scaning_detected = 0

        if rst_count >= 10 and port_scaning_detected == 0:
            detected_scans_amount += 1
            port_scaning_detected = 1
            print(f"prawdopodobny skan portów poraz {detected_scans_amount}")
    print(detected_scans_amount, f"porty hosta były skanowane {detected_scans_amount} razy (ponad 50% ostatnich pakietów ma flagę RST)")

if __name__ == '__main__':
    print("Test filtrowania pliku PCAP:\n")
    #main() Network.pcap --display_filter "http"