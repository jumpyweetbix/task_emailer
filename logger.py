from datetime import datetime

class Logger:
    def __init__(self, todays_date, log_dir):
        self.filename = f"{log_dir}/log_{todays_date}.txt"

    def write_to_file(self, content):
        with open(self.filename, "a+") as fn:
            now = datetime.now().strftime('%d-%m-%y %H:%M:%S')
            fn.write(f"{now} - {content}\n")

    def error(self, msg):
        self.write_to_file(f"ERROR - {msg}")

    def success(self, msg):
        self.write_to_file(f"SUCCESS - {msg}")

    def log(self, msg):
        self.write_to_file(f"LOG - {msg}")



