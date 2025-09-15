from LoggingSystem.LogAppender import LogAppender
from LoggingSystem.LogMessage import LogMessage

class FileAppender(LogAppender):
    def __init__(self,filepath):
        self.filepath=filepath
    
    def append(self,logmessage:LogMessage):
        try:
            #here the writer will write the message 
            with open(self.filepath,"a",encoding="utf8")as writer:
                writer.write(str(logmessage)+"\n")
        except Exception as e:
            print(f"Error writing log to file:{e}")
            
        
        
    