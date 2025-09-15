
from LoggingSystem.LogHandler import LogHandler

class ErrorHandler(LogHandler):
    def __init__(self, level, appender):
        super().__init__(level, appender)
    
    def write(self,message:str):
        print(f"ERROR:{message}")
    
    