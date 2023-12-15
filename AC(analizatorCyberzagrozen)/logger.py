from datetime import datetime

class Logger:
    def __init__(self, log_file="log.txt"):
        self.log_file = log_file

    def output(self, *argv):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as file:
            string = f"[{current_datetime}]"
            for arg in argv:
                string = string + " " + str(arg)
            file.write(string + "\n")
            print(string)
