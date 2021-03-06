from pathlib import Path
from typing import Optional
import logging

PACKAGE_ROOT_DIR = Path(__file__).parent.resolve()
TICKS_DATA_DIR = PACKAGE_ROOT_DIR / './PackageData/.TicksData'
MODEL_FILES_DIR = PACKAGE_ROOT_DIR / './PackageData/ModelFiles'
LIVE_TRADE_FILES_DIR = PACKAGE_ROOT_DIR / './PackageData/.LiveTradingFiles'
TEMP_DIR = PACKAGE_ROOT_DIR / './PackageData/.temp'

LOGGER_LEVELS = {
    'CRITICAL': 50,
    'ERROR': 40,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
    'NOTSET': 0,
}


class Logger:
    __logger_instance = None

    @staticmethod
    def get_instance():
        if Logger.__logger_instance is None:
            logging.basicConfig(format=('%(filename)s: '
                                        '%(levelname)s: '
                                        '%(funcName)s(): '
                                        '%(lineno)d:\t'
                                        '%(message)s'))
            Logger.__logger_instance = logging.getLogger(__name__)
        return Logger.__logger_instance


def set_root_logger_level(level):
    logging.getLogger().setLevel(level=level)


def create_folder(path):
    path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    return path.resolve()


def create_public_package_folders():
    get_model_files_dir()


def get_ticks_data_dir():
    return create_folder(TICKS_DATA_DIR)


def get_model_files_dir():
    return create_folder(MODEL_FILES_DIR)


def get_live_trade_files_dir():
    return create_folder(LIVE_TRADE_FILES_DIR)


def get_temp_dir():
    return create_folder(TEMP_DIR)
