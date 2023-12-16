def example_local_rule(**kwargs):
    condition = False
    # Function body - rule operating on data from kwargs
    # Process pcap
    #for pcap in kwargs.get('pcap', []):
        # Processing logic for pcap files

    # Process evtx
    #for evtx in kwargs.get('evtx', []):
        # Processing logic for evtx files

    # Process xml
    #for xml in kwargs.get('xml', []):
        # Processing logic for xml files

    # Process json
    for json_file in kwargs.get('json', []):
        condition = True
        # Processing logic for json files

    # Process txt
    #for txt in kwargs.get('txt', []):
        # Processing logic for txt files

    # Final rule - what needs to be executed
    if condition:
        action_alert = "local"  # action: "local", "remote"
        description = "Alert json files found"
    else:
        action_alert = None
        description = None
    return action_alert, description

def example_remote_rule(**kwargs):
    condition = False
    # Function body - rule operating on data from kwargs
    # Process pcap
    #for pcap in kwargs.get('pcap', []):
        # Processing logic for pcap files

    # Process evtx
    for evtx in kwargs.get('evtx', []):
        condition = True
        # Processing logic for evtx files

    # Process xml
    #for xml in kwargs.get('xml', []):
        # Processing logic for xml files

    # Process json
    #for json_file in kwargs.get('json', []):
        # Processing logic for json files

    # Process txt
    #for txt in kwargs.get('txt', []):
        # Processing logic for txt files

    # Final rule - what needs to be executed
    if condition:
        action_alert = "remote"  # action: "local", "remote"
        description = "Alert evts file found"
    else:
        action_alert = None
        description = None
    return action_alert, description

def check_for_prohibited_ips(**kwargs):
    import Evtx.Evtx as evtx
    import pyshark
    import re
    import os
    directory_path = os.path.dirname(__file__)
    file_path = os.path.join(directory_path, "list_of_prohibited_ips")
    
    try:
        ip_file = open(file_path, "r")
        prohibited_ips = ip_file.read().splitlines()
        print(f"Searching for Prohibited IPs: {prohibited_ips}")
    except FileNotFoundError:
        print('Prohibitet Ip list not found, create "list_of_prohibited_ips" file')
        return

    alert_action = "remote"
    blocked_ips = []
    details = ""
    detected = False

    ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    
    for scanned_pcap in kwargs.get('pcap', []):
        found_ips = []
        packets = pyshark.FileCapture(scanned_pcap)
        for packet in packets:
            if hasattr(packet, "IP") and hasattr(packet["IP"], "dst") and hasattr(packet["IP"], "src"):
                for ip in [packet["IP"].dst, packet["IP"].src]:
                    if ip not in found_ips and ip in prohibited_ips:
                        detected = True
                        blocked_ips.append(ip)
                        details += f"Prohibited IP {ip} found in file {scanned_pcap}\n"
                        found_ips.append(ip)

    
    for scanned_txt in kwargs.get('txt', []) + kwargs.get('json', [])+ kwargs.get('xml', []):
        try:
            content = open(scanned_txt, mode="r").read()
            ip_list = list(set(ip_pattern.findall(content)))
            for ip in ip_list:
                if ip in prohibited_ips:
                    detected = True
                    blocked_ips.append(ip)
                    details += f"Prohibited IP {ip} found in file {scanned_txt}\n"
        except Exception:
            pass
    
    for scanned_evtx in kwargs.get('evtx', []):
        event_data = ""
        try:
            with evtx.EventFile(scanned_evtx) as event_log:
                for record in event_log.records():
                    for item in record.xml():
                        event_data += item
                ip_list = list(set(ip_pattern.findall(event_data)))
                for ip in ip_list:
                    if ip in prohibited_ips:
                        detected = True
                        blocked_ips.append(ip)
                        details += f"Prohibited IP {ip} found in file {scanned_evtx}\n"
        except Exception:
            pass

    if not detected:
        alert_action = None
        blocked_ips = None
        details = None

    return alert_action, details
