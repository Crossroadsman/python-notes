import logging

logging.basicConfig(
    level=logging.DEBUG“, 
    format=' %(asctime)s - %(levelname)s - %(message)s”
)

logging.debug("Start of program")

def my_function():
    logging.debug("entered function")
    ...

