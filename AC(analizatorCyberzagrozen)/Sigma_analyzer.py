# Przykład wywołania Zircolite z Pythona
# Zakładając, że Zircolite i reguły SIGMA są już zainstalowane i skonfigurowane

import subprocess

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

# Ścieżki do plików
evt_log_path = "OldTestData/WinDefender_Events_1117_1116_AtomicRedTeam.evtx"
sigma_rules_path = "OldTestData/rules/rules_windows_generic_full.json"



# Uruchomienie Zircolite
run_zircolite_evtx(evt_log_path, sigma_rules_path)

# Przetworzenie wyników...
