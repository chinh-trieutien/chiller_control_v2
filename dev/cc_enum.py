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


class DefinitionRowType(Enum):
    NONE = -1
    IS_EMPTY = 1
    IS_HEADER = 2
    IS_DATA_ROW = 3


class TemperatureType(Enum):
    NONE = -1
    IS_GOOD = 1
    IS_TOOHIGH = 2
    IS_TOOLOW = 3


class LoadType(Enum):
    NONE = -1
    LOAD = 1
    TIMELINE = 2
    TEMPERATURE = 3


class BuiltinRunOptions(Enum):
    NONE = -1
    NEW_CHILLER_DATABASE = 1
    NEW_LOAD_DATABASE = 2
    CONSTRAINT_TE = 3
    CONSTRAINT_TC = 4


class BuiltinInputOptions(Enum):
    NONE = -1
    DEFAULT_INPUT = 1
    USER_MODEL = 2
    USER_CHILLER_LIST = 3


class InterpolateMode(Enum):
    NONE = -1
    SINGLE_VALUE = 1
    INTERPOLATE_ROW = 2
    INTERPOLATE_COLUMN = 3
