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