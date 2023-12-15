''' GEN.MGMT.1 Opracować aplikację w języku Python z interfejsem CLI,
która pozwoli na realizację
 wskazanych wymagań. Moduł do tworzenia aplikacji CLI - Click'''
import click
import os
import pythonAnalyzer as AN
import Sigma_analyzer as SIGMA
import txt_log_analyzer as TLA
from click_shell import shell
from PCAP_analyzer import Pcap_analyzer, get_available_pcap_files

# @click.group()  # no longer
@shell(prompt='my-app > ', intro='Starting my app...')
def my_app():
    pass

@my_app.command()
@click.option('--path','-p', help='Path to rules',show_default=True,type=click.Path(exists=True),nargs=1,default='offline_analyzer/detection-rules.py',required=False)
def load_python_rules(path):
    global python_rules
    print("Loading rules")
    python_rules = AN.load_rules(path)
    count_rules=AN.count_rules(python_rules)
    print(count_rules,"Rules loaded")

@my_app.command()
@click.option('--load-rules',help='Path to rules to load',type=click.Path(exists=True),nargs=1,required=False)
def show_python_rules(load_rules):
    if load_rules is not None:
        print("Loading rules")
        global python_rules
        python_rules=AN.load_rules(load_rules)
        count_rules=AN.count_rules(python_rules)
        print(count_rules,"Rules loaded")
    try: python_rules
    except NameError:
        print("Load rules first")
    else:
        print("List of loaded rules:")
        AN.show_rules(python_rules)

@my_app.command()
@click.option('--path','-p', prompt='Path to scan',help='Path to scan',type=click.Path(exists=True),nargs=1,required=True)
@click.option('--load-rules',help='Path to rules to load',type=click.Path(exists=True),nargs=1,required=False)
@click.option('--rule-name',help='name of rule to load',nargs=1,required=False)
def use_python_rule(path,load_rules,rule_name):
    if load_rules is not None:
        print("Loading rules")
        global python_rules
        python_rules=AN.load_rules(load_rules)
        count_rules=AN.count_rules(python_rules)
        print(count_rules,"Rules loaded")
    try: python_rules
    except NameError:
        print("Load rules first")
    else:
        AN.process_files_with_rules(python_rules,path,rule_name)

#----Scenariusz2----
@my_app.command()
@click.option('--pattern')
@click.option('--file_paths', nargs=1, type=click.Path(exists=True))
def grep_command(pattern, file_paths):
    """Search for PATTERN in each FILE_PATH using grep."""
    results = TLA.grep_in_files(pattern, file_paths)
    print(results)

@my_app.command()
@click.option('--pattern')
@click.option('--file_paths', nargs=1, type=click.Path(exists=True))
def regex_command(pattern, file_paths):
    """Search for PATTERN in each FILE_PATH using Python regular expressions."""
    results = TLA.re_search_in_files(pattern, file_paths)
    print(results)


#------SIGMA--------
@my_app.command()
@click.option('--evt_log_path',help='Path to evt file to load',type=click.Path(exists=True),nargs=1,required=True)
@click.option('--sigma_rules_path',help='Path to rules to load',type=click.Path(exists=True),nargs=1,required=True)
def sigmaEvt(evt_log_path, sigma_rules_path):
    SIGMA.run_zircolite_evtx(evt_log_path, sigma_rules_path)
    SIGMA.display_event_data("detected_events.json")

@my_app.command()
@click.option('--json_log_path',help='Path to json file to load',type=click.Path(exists=True),nargs=1,required=True)
@click.option('--sigma_rules_path',help='Path to rules to load',type=click.Path(exists=True),nargs=1,required=True)
def sigmaEvt(json_log_path, sigma_rules_path):
    SIGMA.run_zircolite_json(json_log_path, sigma_rules_path)
    SIGMA.display_event_data("detected_events.json")

@my_app.command()
@click.option('--events', type=click.Path(exists=True))
def display_events_command(events):
    """Display event data from a JSON file."""
    if events is not None:
        SIGMA.display_event_data(events)
    else:
        SIGMA.display_event_data("detected_events.json")

#----Scenariusz1----
@my_app.command()
@click.option('--pcap_path', prompt='Enter the path to search for PCAP files', type=click.Path(exists=True))
@click.option('--display_filter', prompt='Enter BPF display filter (press Enter for no filter)', default="")
def analyze_pcap_interactive(pcap_path, display_filter):
    """
    Click command to interactively analyze a PCAP file with filter options.
    """
    click.echo("Welcome to interactive PCAP analysis!")
    # Get the list of available PCAP files
    available_pcap_files = get_available_pcap_files(pcap_path)
    pcap_file = click.prompt("Choose a PCAP file", type=click.Choice(available_pcap_files))
    full_path = os.path.join(pcap_path, pcap_file)
    Pcap_analyzer(full_path, display_filter)



if __name__ == '__main__':
    my_app()
