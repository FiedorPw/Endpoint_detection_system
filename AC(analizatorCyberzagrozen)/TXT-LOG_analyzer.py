import subprocess
import shlex
import re


def grep_in_files(pattern, file_paths):

    results = {}
    for file_path in file_paths:
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

    return results

def re_search_in_files(pattern, file_paths):
    results = {}
    compiled_pattern = re.compile(pattern)

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                # Finding all matches
                matches = compiled_pattern.findall(file_content)
                results[file_path] = matches
        except Exception as e:
            results[file_path] = f"Error: {str(e)}"

    return results

def main():
    pattern = "plik"
    file_paths = {"OldTestData/text_read_test.log","OldTestData/ourLog.log"}
    print(grep_in_files(pattern, file_paths))
    # Wyrażenie regularne do wyszukiwania adresów email
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    # Wywołanie funkcji re_search_in_files
    matches = re_search_in_files(email_pattern, file_paths)

    # Wyświetlanie wyników
    for file_path, matching_lines in matches.items():
        print(f"Wyniki dla {file_path}:")
        for line in matching_lines:
            print(line)

if __name__ == '__main__':
    main()
