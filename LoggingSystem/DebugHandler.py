
from LoggingSystem.LogHandler import LogHandler

class DebugHandler(LogHandler):
    def __init__(self, level, appender):
        super().__init__(level, appender)
    
    def write(self,message:str):
        print(f"DEBUG:{message}")
        
    