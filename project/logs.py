import logging


import config
#logging.basicConfig()

#todo fix root dir being variable
logger = logging.getLogger(__name__)
format = '%(asctime)s|%(name)s|%(levelname)s|%(message)s (%(filename)s:%(lineno)d)'
f_format = logging.Formatter(format)
#logging.basicConfig(filename=f'{config.ROOT_DIR}/../logs/logtest.log',filemode='a', level=logging.DEBUG, format=format)
f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.error("test")