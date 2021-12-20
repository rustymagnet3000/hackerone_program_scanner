import sys
from src.main import main
from conf.base_logger import logger

if __name__ == '__main__':
    logger.info('Starting...')
    sys.exit(main())
    logger.info('End of program')
