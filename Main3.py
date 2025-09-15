#here the first step is to create the chain of loggers 
from LoggingSystem.LogAppender import LogAppender
from LoggingSystem.ErrorHandler import ErrorHandler
from LoggingSystem.LogHandler import LogHandler
from LoggingSystem.InfoHandler import InfoHandler
from LoggingSystem.DebugHandler import DebugHandler
from LoggingSystem.ConsoleAppender import ConsoleAppender
from LoggingSystem.FileAppender import FileAppender
from LoggingSystem.Logger import Logger
from LoggingSystem.LoggingLevel import LoggingLevel
from LoggingSystem.LoggerConfig import LoggerConfig
from LoggingSystem.enums.Message import Message



def get_chain_of_loggers(appender:LogAppender):
    errorlogger=ErrorHandler(Message.ERROR,appender)
    infologger=InfoHandler(Message.INFO,appender)
    debuglogger=DebugHandler(Message.DEBUG,appender)
    
    #now lets set the nextlogger as the info sets to debug,debug sets to error
    infologger.setNextlogger(debuglogger)
    #now debuglogger will set to errorlogger
    debuglogger.setNextlogger(errorlogger)
    return infologger
    
if __name__ == "__main__":
    #lets first find the consoleappender
    consoleappender=ConsoleAppender()
    fileappender=FileAppender("log.txt")
    
    #now create chain of loggers
    loggerchain=get_chain_of_loggers(consoleappender)
    #info
    print("Logging INFO level message")
    loggerchain.logMessage(Message.INFO,"This is an info message")
    #debug 
    print("Logging DEBUG level message")
    loggerchain.logMessage(Message.DEBUG,"This is debug message")
    #error
    print("Logging ERROR level message")
    loggerchain.logMessage(Message.ERROR,"This is a error message")
    
    print("\nUsing Singleton Logger:")
    logger = Logger.get_instance(Message.INFO, consoleappender)
    logger.set_config(LoggerConfig(Message.INFO, fileappender))
    logger.error("Using singleton Logger - Error message")
    
    
    
    