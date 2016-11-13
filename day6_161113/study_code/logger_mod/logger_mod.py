import logging


# logging.warning("what a fucking days !!")
# logging.critical("what a cretical days!!")

logging.basicConfig(format='%(asctime)s  %(levelname)s %(message)s',
                    filename='access.log',level=logging.DEBUG)

logging.debug("wo shi debug")
logging.info("wo shi info")

