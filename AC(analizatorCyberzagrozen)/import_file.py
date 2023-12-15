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
import xml.etree.ElementTree as ET
import json
from Evtx.Evtx import Evtx
from Evtx.Views import evtx_record_xml_view
from logger import Logger

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
        return ET.tostring(tree.getroot(), encoding='utf-8').decode('utf-8') 
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

def read_evtx_file(filename):
    output_filename = 'OldTestData/output.xml'
    evtx_content = ""
    try:
        with Evtx(filename) as evtx:
            for record in evtx.records():
                xml_str = evtx_record_xml_view(record)
                evtx_content += f'{xml_str}\n'
            log_to_file("read_evtx_file read file in xml")

            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(evtx_content)

    except Exception as e:
        print(f"Error reading the EVTX file: {e}")
    return evtx_content

def log_to_file(message):
    Logger.output(message)

def import_pcap(filename, display_filter=None):
    if display_filter:
        capture = pyshark.FileCapture(filename, display_filter=display_filter)
        log_to_file("import_pcap read file with display filter: {display_filter}")
    else:
        capture = pyshark.FileCapture(filename)
    return capture

def analyze_pcap_packets(capture):
    for packet in capture:
        print(packet)

if __name__ == "__main__":
    read_json = read_json_file('OldTestData/test.json')#json_read_test.log
    print("test jsona:",read_json, "\n")

    read_xml = read_xml_file('OldTestData/test.xml')#xml_read_test.logtest.xml
    print("test xmla:\n",read_xml, "\n")

    read_txt = read_txt_file('OldTestData/text_read_test.log')
    print("test txt:", read_txt, "\n")

    read_evtx = read_evtx_file('OldTestData/LM_sysmon_remote_task_src_powershell.evtx')
    print("test evtxa:\n", read_evtx)

#capture = import_pcap('Network.pcap')

#if read_xml is not None:

#    for book_element in read_xml.findall('book'):
#       book_id = book_element.get('id')
#       author = book_element.find('author').text
#       title = book_element.find('title').text
#        genre = book_element.find('genre').text
#       price = book_element.find('price').text
#        publish_date = book_element.find('publish_date').text
#       description = book_element.find('description').text

#        print(f"Book ID: {book_id}")
#        print(f"Author: {author}")
#        print(f"Title: {title}")
#        print(f"Genre: {genre}")
#        print(f"Price: {price}")
#        print(f"Publish Date: {publish_date}")
#        print(f"Description: {description}\n")

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
