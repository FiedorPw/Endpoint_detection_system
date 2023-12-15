'''
OFF.DETPY.1.3 Informacjami zwrotnymi z reguły są:
action_alert - jedna z dwóch akcji alertujących z grupy:
local - oznacza wypisanie informacji o zdarzeniu na CLI oraz do loga
remote - oznacza to samo co local oraz wysłanie informacji po REST API do aplikacji
Zdalnego Kolektora Zdarzeń (Wymagania GEN.MGMT.5 , GEN.LOG.1 )

description - opis tekstowy według przyjętego formatu, może to być także JSON, XML czy
syslog.
'''

import importlib.util
import os
import networkClient as nc

def show_rules(rules_module):
    for rule_name in dir(rules_module):
        if not rule_name.startswith("__") and not rule_name.endswith("__"):
            print(rule_name)
def count_rules(rules_module):
    count = 0
    for rule_name in dir(rules_module):
        if not rule_name.startswith("__") and not rule_name.endswith("__"):
            count = count + 1
    return count
def load_rules(file_path):
    spec = importlib.util.spec_from_file_location("detection_rules", file_path)
    detection_rules = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(detection_rules)
    return detection_rules

def process_files_with_rules(rules_module, folder_path,rule_name_to_use=None):
    files = {}
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1][1:]
            files.setdefault(file_extension, []).append(os.path.join(root, filename))

    # Execute rules on the collected files
    for rule_name in dir(rules_module):
        if rule_name_to_use is None or rule_name_to_use == rule_name:
            rule_function = getattr(rules_module, rule_name)
            if callable(rule_function):
                action_alert, description = rule_function(**files)
                # Perform actions based on the rule output
                if action_alert:
                    if action_alert == "local":
                        print(f"Rule: {rule_name}, Action: {action_alert}, Description: {description}")
                        # Log information locally
                    elif action_alert == "remote":
                        print(f"Rule: {rule_name}, Action: {action_alert}, Description: {description}")
                        nc.sendRuleDetection(rule_name=rule_name,description=description)
                        # Log information locally and send information via REST API
                else:
                    print("No action needed for this rule.")
