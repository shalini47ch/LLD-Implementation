#here we will have log level and logappender
from LoggingSystem.LoggingLevel import LoggingLevel
from LoggingSystem.LogAppender import LogAppender


class LoggerConfig:
    def __init__(self,loglevel:LoggingLevel,logappender:LogAppender):
        #it will have loglevel and logappender
        self.loglevel=loglevel
        self.logappender=logappender
    
    #now creating getter and setter for that
    def getLogLevel(self):
        return self.loglevel 
    
    def setLogLevel(self,loglevel):
        self.loglevel=loglevel
    
    #similarly create for getlogAppender and setlogAppender
    def getLogAppender(self):
        return self.logappender
    
    def setLogAppender(self,logappender):
        self.logappender=logappender
    
        

        
    