import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    # above s is given to treat it as string so that concatenation can happen
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  ##file handler object
    logger.setLevel(logging.INFO)
   # logger.debug("A debug statement is executed")
   # logger.info("An Information statement")
   # logger.warning("something is in warning mode ")
   # logging.error("A major error has happened")
   # logger.critical("Critical Issue")
