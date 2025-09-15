import threading 
from LoggingSystem.LoggerConfig import LoggerConfig
from LoggingSystem.enums.Message import Message
from LoggingSystem.LogAppender import LogAppender 
from LoggingSystem.LogMessage import LogMessage

class Logger:
    _instances = {}                 
    _lock = threading.Lock()        

    def __init__(self, log_level: Message, log_appender: LogAppender):
        self.config = LoggerConfig(log_level, log_appender)

    @classmethod
    def get_instance(cls, log_level: Message, log_appender: LogAppender):
        key = f"{log_level.name}_{log_appender.__class__.__name__}"
        with cls._lock:
            if key not in cls._instances:
                cls._instances[key]=Logger(log_level, log_appender)
            return cls._instances[key]
        
    def set_config(self, config: LoggerConfig):
        with Logger._lock:
            self.config = config

    def log(self, level: Message, message: str):
        if level.value >= self.config.loglevel.value:
            log_message = LogMessage(level, message)
            self.config.logappender.append(log_message)

    # Convenience methods
    def debug(self, message: str):
        self.log(Message.DEBUG, message)

    def info(self, message: str):
        self.log(Message.INFO, message)

    def error(self, message: str):
        self.log(Message.ERROR, message)
