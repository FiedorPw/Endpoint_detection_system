''' GEN.MGMT.1 Opracować aplikację w języku Python z interfejsem CLI,
która pozwoli na realizację
 wskazanych wymagań. Moduł do tworzenia aplikacji CLI - Click'''
import click
import pythonAnalyzer as AN
from click_shell import shell

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

if __name__ == '__main__':
    my_app()
