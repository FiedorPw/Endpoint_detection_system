import click
from import_file import log_to_file, import_pcap, analyze_pcap_packets

@click.command()
@click.argument('pcap_file', type=click.Path(exists=True))
@click.option('--display_filter', help='BPF display filter for PCAP analysis')
def main(pcap_file, display_filter):
    """
    Cyber Threat Analyzer CLI
    """
    log_to_file(f"Analyzing PCAP file: {pcap_file}")

    # Import PCAP file with optional display filter
    capture = import_pcap(pcap_file)

    # Analyze PCAP packets
    analyze_pcap_packets(capture)

if __name__ == '__main__':
    main()