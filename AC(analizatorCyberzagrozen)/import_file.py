'''
GEN.MGMT.3 Aplikacja ma możliwość wskazania pojedynczych plików, folderu lub grupy folderów do
przeszukania w poszukiwaniu plików, które mają być wykorzystane do analizy

GEN.MGMT.4 Obsługiwane formaty wejściowe plików do analizy:
-pliki tekstowe w formatach .txt , .xml , .json
-pliki ze zrzutami ruchu PCAP .pcap
-pliki logów Sysmon Windows EVTX - .evtx , przetwarzane na format tekstowy JSON, XML lub
-innych tekstowy (do wyboru według własnego uznania)

OFF.PCAP.1 Analizator Cyberzagrożeń ma możliwość wyświetlania zawartości pakietów z
wczytanych plików PCAP.

OFF.PCAP.2 Analizator Cyberzagrożeń ma możliwość przekazania filtru zgodnego z formatem BPF
(wykorzystywanego przez libpcap / tshark / pyshark / Wireshark / Scapy ) do funkcji otwierającej i
wczytującej plik PCAP.
'''

import pyshark
import click
import xml.etree.ElementTree as ET
import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            log_to_file("read_json_file read file")
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding the JSON file: {e}")
        return None


def read_xml_file(filename):
    try:
        tree = ET.parse(filename)
        log_to_file("read_xml_file read file")
        return tree
    except ET.ParseError as e:
        print(f"Error parsing the XML file: {e}")
        return None

def read_txt_file(filename):
    try:
        with open(filename, 'r') as file:
            log_to_file("read_txt_file read file")
            return file.read()
    except IOError as e:
        print(f"Error reading the TXT file: {e}")
        return None


def log_to_file(message):
    with open('OldTestData/ourLog.log', 'a') as file:
        file.write(f'info: {message}\n')

def import_pcap(filename):
    capture = pyshark.FileCapture(filename)
    log_to_file("import_pcap read file")
    return capture

def analyze_pcap_packets(capture):
    for packet in capture:
        print(packet)

read_json = read_json_file('OldTestData/json_read_test.log')
print("test jsona",read_json)


read_xml = read_xml_file('OldTestData/xml_read_test.log')
print("test xmla",read_xml)

read_txt = read_txt_file('OldTestData/text_read_test.log')
print("test txt", read_txt)

#capture = import_pcap('Network.pcap')


#test pcap

# for packet in capture:
#     print(packet)  # Prints out a summary of each packet

# first_packet = capture[0]
# first_packet_ip = capture[0].ip
#
# print("\n____________________________\n", first_packet)
# print("\n____________________________\n", first_packet_ip)
#
# # wykrywanie ip które zapodaje sporo SYN
# for packet in capture:
#     if 'TCP' in packet and packet.tcp.flags_syn == '1' and packet.tcp.flags_ack == '0':
#         print(f"Possible SYN Flood attack packet: {packet.ip.src} -> {packet.ip.dst}")
