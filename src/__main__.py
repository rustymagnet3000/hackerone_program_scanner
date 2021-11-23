import sys
from src.main import main
from src.base_logger import logger

if __name__ == '__main__':
    logger.info(f'Starting...')
    sys.exit(main())

