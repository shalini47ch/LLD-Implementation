from LoggingSystem.LogHandler import LogHandler

class InfoHandler(LogHandler):
    def __init__(self, level, appender):
        super().__init__(level, appender)
    
    def write(self,message:str):
        print(f"INFO {message}")
    
    
    #here we have the implementation of LogHandler abstract class
    
    
        
    