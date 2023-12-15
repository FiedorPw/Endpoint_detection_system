from import_file import log_to_file, import_pcap, analyze_pcap_packets
import os

#@click.argument('pcap_file', type=click.Path(exists=True))
#@click.option('--display_filter', help='BPF display filter for PCAP analysis')
def Pcap_analyzer(pcap_file, display_filter):

    log_to_file(f"Analyzing PCAP file: {pcap_file}")

    # Import PCAP file
    capture = import_pcap(pcap_file, display_filter)

    analyze_pcap_packets(capture)

def get_available_pcap_files(path):
    """
    Get the list of PCAP files in the specified path.
    """
    pcap_files = [file for file in os.listdir(path) if file.endswith('.pcap')]
    return pcap_files

if __name__ == '__main__':
    print("Test filtrowania pliku PCAP:\n")
    #main() Network.pcap --display_filter "http"