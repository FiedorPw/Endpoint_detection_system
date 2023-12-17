from datetime import datetime

class Logger:
    def __init__(self, log_file="log.txt"):
        Logger.log_file = log_file
    @staticmethod
    def output(*argv):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Logger.log_file, "a") as file:
            string = f"[{current_datetime}]"
            for arg in argv:
                string = string + " " + str(arg)
            file.write(string + "\n")
            print(string)
            return string
