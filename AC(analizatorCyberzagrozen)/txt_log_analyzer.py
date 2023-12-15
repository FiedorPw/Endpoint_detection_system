import subprocess
import shlex
import re
import os

def grep_in_files(pattern, paths):
    results = {}

    for path in paths:
        if os.path.isfile(path):  # Check if it's a file
            try:
                # Constructing the grep command
                command = f"grep -n {shlex.quote(pattern)} {shlex.quote(path)}"
                # Executing the command
                result = subprocess.run(command, shell=True, text=True, capture_output=True)
                # Parsing the output
                matches = result.stdout.split('\n') if result.stdout else []
                results[path] = matches
            except Exception as e:
                results[path] = [f"Error: {str(e)}"]
        elif os.path.isdir(path):  # Check if it's a directory
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        # Constructing the grep command
                        command = f"grep -n {shlex.quote(pattern)} {shlex.quote(file_path)}"
                        # Executing the command
                        result = subprocess.run(command, shell=True, text=True, capture_output=True)
                        # Parsing the output
                        matches = result.stdout.split('\n') if result.stdout else []
                        results[file_path] = matches
                    except Exception as e:
                        results[file_path] = [f"Error: {str(e)}"]
        else:
            results[path] = "Error: Path is neither a file nor a directory."

    return results

def re_search_in_files(pattern, paths):
    results = {}
    compiled_pattern = re.compile(pattern)

    for path in paths:
        if os.path.isfile(path):  # Check if it's a file
            try:
                with open(path, 'r') as file:
                    file_content = file.read()
                    matches = compiled_pattern.findall(file_content)
                    results[path] = matches
            except Exception as e:
                results[path] = f"Error: {str(e)}"
        elif os.path.isdir(path):  # Check if it's a directory
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as file:
                            file_content = file.read()
                            matches = compiled_pattern.findall(file_content)
                            results[file_path] = matches
                    except Exception as e:
                        results[file_path] = f"Error: {str(e)}"
        else:
            results[path] = "Error: Path is neither a file nor a directory."

    return results


def main():
    pattern = "plik"
    file_paths = {"OldTestData/text_read_test.log","OldTestData/ourLog.log","OldTestData/output.xml"}
    print(grep_in_files(pattern, file_paths))
    # Wyrażenie regularne do wyszukiwania adresów email
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    
    file_paths = {"OldTestData/text_read_test.log","OldTestData/ourLog.log"}
    # Wywołanie funkcji re_search_in_files
    print(re_search_in_files(email_pattern, file_paths))


if __name__ == '__main__':
    main()
