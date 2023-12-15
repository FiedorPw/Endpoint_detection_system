import importlib.util
import os

def load_rules(file_path):
    spec = importlib.util.spec_from_file_location("detection_rules", file_path)
    detection_rules = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(detection_rules)
    return detection_rules

def process_files_with_rules(rules_module, folder_path):
    files = {}
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1][1:]
            files.setdefault(file_extension, []).append(os.path.join(root, filename))

    # Execute rules on the collected files
    for rule_name in dir(rules_module):
        rule_function = getattr(rules_module, rule_name)
        if callable(rule_function):
            action_alert, description = rule_function(**files)
            # Perform actions based on the rule output
            if action_alert:
                print(f"Action: {action_alert}, Description: {description}")
            else:
                print("No action needed.")

if __name__ == "__main__":
    rules_file_path = "path/to/detection-rules.py"  # Replace with the correct path
    folder_to_analyze = "path/to/folder"  # Replace with the folder path containing the files to analyze

    rules = load_rules(rules_file_path)
    process_files_with_rules(rules, folder_to_analyze)
