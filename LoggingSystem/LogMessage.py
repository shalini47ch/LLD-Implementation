from LoggingSystem.enums.Message import Message
import time

class LogMessage:
    #it is have the things like level,content and timestamp
    def __init__(self,level:Message,message:str):
        self.level=level
        self.message=message
        self.timestamp=int(time.time()*1000)
    
    def getlevel(self):
        return self.level 
    
    def getMessage(self):
        return self.message
    
    def getTimestamp(self):
        return self.timestamp
    #now at last printing the level
    
    def __str__(self):
        return f"[{self.level.name}] {self.timestamp}:{self.message}"
    


    
    
        
    
    