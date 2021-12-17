import logging
import sys
import colorlog

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(colorlog.ColoredFormatter('%(log_color)s [%(asctime)s] %(levelname)s[*]%(message)s', datefmt='%a, %d %b %Y %H:%M:%S'))
logger.addHandler(sh)
