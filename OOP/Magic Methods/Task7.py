import datetime
from contextlib import ContextDecorator

class LogFile(ContextDecorator):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.datetime.now()
        execution_time = end_time - self.start_time
        log_entry = f"Start: {self.start_time} | Run: {execution_time} | An error occurred: {exc_value}"
        
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(log_entry + "\n")

        return exc_type is None

    def log(self, message):
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(message + "\n")  


@LogFile('my_trace.log')
def some_func():
    for i in range(5):
        print(i)
        for k in range(10):
            print(k)
            for j in range(3):
                print(j + k + i)
    #print(1/0)

some_func()