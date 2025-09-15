
from LoggingSystem.LogAppender import LogAppender
from LoggingSystem.LogMessage import LogMessage

class ConsoleAppender(LogAppender):
    def append(self,logmessage:LogMessage):
        print(logmessage)
    