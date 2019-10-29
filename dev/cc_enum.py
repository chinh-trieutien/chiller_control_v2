import os
import os.path as op

from enum import Enum

root = op.dirname(os.getcwd())

INPUT = root + "\\input\\"

RAW_PATH = INPUT + "\\raw\\"
DEFAULT_PJ_INFO_PATH = RAW_PATH + "\\project_info.csv"

CHILLER_PATH = RAW_PATH + "\\chiller\\chiller_list.csv"
CATALOGUE_PATH = RAW_PATH + "\\catalogue\\"
CALCULATED_LOAD_PATH = RAW_PATH + "\\calculated\\"
WEATHERFILE_PATH = RAW_PATH + "\\weatherfile\\"

RESOURCE_PATH = INPUT + "\\analyzed\\"

GENERAL_FILE_PATH = RESOURCE_PATH + "GENERAL.pickle"
CHILLER_LIST_PATH = RESOURCE_PATH + "CHILLER_LIST.pickle"
COMBINATIONS_PATH = RESOURCE_PATH + "combinations\\"
# COMBINATIONS_PATH = RESOURCE_PATH + "COMBINATIONS.pickle"


class Row(Enum):
    IS_EMPTY = 0
    IS_HEADER = 1
    IS_DATA_ROW = 2


class Temperature(Enum):
    IS_GOOD = 0
    IS_TOOHIGH = 1
    IS_TOOLOW = 2


class LoadType(Enum):
    NONE = 0
    LOAD = 1
    TIMELINE = 2
    TEMPERATURE = 3


class BuiltinRunOptions(Enum):
    NEW_CHILLER_DATABASE = 0
    NEW_LOAD_DATABASE = 1
    CONSTRAINT_TE = 2
    CONSTRAINT_TC = 3


class BuiltinInputOptions(Enum):
    DEFAULT_INPUT = 0
    USER_MODEL = 1
    USER_CHILLER_LIST = 2


if __name__ == "__main__":

    if Temperature.IS_GOOD:
        print("hi")

    if Temperature.IS_TOOHIGH.value == 1:
        print("hi")
