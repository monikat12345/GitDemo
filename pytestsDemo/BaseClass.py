import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        #logger = logging.getLogger(__name__)
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        # above s is given to treat it as string so that concatenation can happen
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  ##file handler object
        logger.setLevel(logging.DEBUG)
        return logger


