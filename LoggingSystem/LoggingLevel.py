from LoggingSystem.enums.Message import Message 

class LoggingLevel:
    @staticmethod
    def isgreaterequal(level1:Message,level2:Message):
        return level1.value>=level2.value
    