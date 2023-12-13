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

def log_to_file(message):
    with open('ourLog.log', 'a') as file:
        file.write(f'info: {message}\n')

def import_pcap(filename):
    capture = pyshark.FileCapture(filename)
    log_to_file("import_pcap read file")
    return capture



read_json = read_json_file(f'json_read_test.log')
print("test jsona",read_json)


read_xml = read_xml_file('AC(analizatorCyberzagrozen)/OldTestData/xml_read_test.log')
print("test xmla",read_json)

capture = import_pcap('Network.pcap')


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
