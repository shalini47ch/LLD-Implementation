
from abc import ABC,abstractmethod
from LoggingSystem.LoggingLevel import LoggingLevel
from LoggingSystem.LogAppender import LogAppender
from LoggingSystem.LogMessage import LogMessage
from LoggingSystem.enums.Message import Message

class LogHandler(ABC):
    #here the nextlogger helps to maintain the chain of responsibility design pattern
    def __init__(self,level:LoggingLevel,appender:LogAppender):
        self.level=level
        self.nextlogger=None
        self.appender=appender
    
    def setNextlogger(self,nextlogger):
        self.nextlogger=nextlogger 
    
    #create a helper function to log message with filter and chaining
    def logMessage(self,level:Message,message:LogMessage):
        if self.level.value>=level.value:
            logmsg=LogMessage(level,message)
            if self.appender:
                self.appender.append(logmsg)
            self.write(message)
        #if the value is not greater then you move to the next logger
        elif self.nextlogger:
            self.nextlogger.logMessage(level,message)
    @abstractmethod
    def write(self,message:str):
        pass
        
        
    
    
        
        
    
    