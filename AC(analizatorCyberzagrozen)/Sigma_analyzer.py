# Przykład wywołania Zircolite z Pythona
# Zakładając, że Zircolite i reguły SIGMA są już zainstalowane i skonfigurowane

import subprocess
import json

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def run_zircolite_json(evt_log_path, sigma_rules_path):
    command = [
        "python3", "zircolite.py", 
        "--events", evt_log_path,
        "--ruleset", sigma_rules_path,
        "--jsonl"
    ]
    
    return subprocess.run(command)
    
    
def run_zircolite_evtx(evt_log_path, sigma_rules_path):

    
    command = [
        "python3", "zircolite.py", 
        "--evtx", evt_log_path,
        "--ruleset", sigma_rules_path
        
    ]
    return subprocess.run(command)
    
    
def display_event_data(events):
    json_data = load_json_data(events)
    for event in json_data[:-1]:
        rule_level = event.get("rule_level", "No title")
        title = event.get("title", "No title")
        description = event.get("description", "No description")
        count = event.get("count", 0)
        print(f"Level: {rule_level}\nTitle: {title}\nDescription: {description}\nCount: {count}\n")


if __name__ == '__main__':
    # Ścieżki do plików
    evt_log_path = "OldTestData/WinDefender_Events_1117_1116_AtomicRedTeam.evtx"
    sigma_rules_path = "OldTestData/rules/rules_windows_generic_full.json"
    events="detected_events.json"
    
    # Uruchomienie Zircolite
    run_zircolite_evtx(evt_log_path, sigma_rules_path)
    display_event_data(events)
    
    # Przetworzenie wyników...
    