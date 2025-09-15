#logappender is of two types file appender and console appender
from abc import ABC,abstractmethod 
from LoggingSystem.LogMessage import LogMessage

class LogAppender(ABC):
    @abstractmethod
    def append(logMessage:LogMessage):
        pass
