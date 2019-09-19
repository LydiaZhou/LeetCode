class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logDict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.logDict:
            if self.logDict[message] + 10 <= timestamp:
                self.logDict[message] = timestamp
                return True
            else:
                return False
        self.logDict[message] = timestamp
        return True

# Your Logger object will be instantiated and called as such:
if __name__ == '__main__':
    logger =  Logger();
    print(logger.shouldPrintMessage(1, "foo"))
    print(logger.shouldPrintMessage(2, "bar"))
    print(logger.shouldPrintMessage(10, "foo"))
    print(logger.shouldPrintMessage(11, "foo"))