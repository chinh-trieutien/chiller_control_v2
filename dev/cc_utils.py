import time
import datetime

from copy import deepcopy

from cc_enum import InterpolateMode
from cc_chiller import Table

debug = True
# debug = False


class Utils(object):

    class Common():
        @staticmethod
        def print_debug(msg, debug=False, debug_level=3):
            if debug:
                print(datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"), msg)
                time.sleep(0.5)

        @staticmethod
        def RowValidate(row):
            if any(row):
                if '' in row:
                    return Row.IS_HEADER
                else:
                    return Row.IS_DATA_ROW
            else:
                return Row.IS_EMPTY

    # @staticmethod
    class Interpolate():

        @staticmethod
        def RowValidate(table=None, row=None):
            if row >= table.RowHeaderMin and row <= table.RowHeaderMax:
                return True
            else:
                return False

        @staticmethod
        def ColumnValidate(table=None, column=None):
            if column >= table.ColumnHeaderMin and column <= table.ColumnHeaderMax:
                return True
            else:
                return False

        @staticmethod
        def TableValidate(table=None, row=None, column=None):
            if table is Table:
                interpolatable = False
                Utils.Common.print_debug(
                    "Table suppose tobe Table object only", debug=debug)
            elif table.Level != 2:
                interpolatable = False
                Utils.Common.print_debug(
                    "Table level have to equal to 2", debug=debug)
            elif (row is None) & (column is None):
                interpolatable = False
                Utils.Common.print_debug(
                    "Nothing to lookup", debug=debug)
            elif row is None:
                if Utils.Interpolate.ColumnValidate(table=table, column=column):
                    interpolatable = True
                    interpolate_mode = InterpolateMode.INTERPOLATE_COLUMN
                    Utils.Common.print_debug(
                        "Interpolate all col_{}".format(column), debug=debug)
                else:
                    interpolatable = False
                    Utils.Common.print_debug(
                        "Chosen column out of range: col_{}".format(column), debug=debug)

            elif column is None:
                if Utils.Interpolate.RowValidate(table=table, row=row):
                    interpolatable = True
                    interpolate_mode = InterpolateMode.INTERPOLATE_ROW
                    Utils.Common.print_debug(
                        "Interpolate all row_{}".format(row), debug=debug)
                else:
                    interpolatable = False
                    Utils.Common.print_debug(
                        "Chosen row out of range: row_{}".format(row), debug=debug)
            elif not((row is None) & (column is None)):
                interpolatable = True
                if not(Utils.Interpolate.RowValidate(table=table, row=row)):
                    interpolatable = False
                    Utils.Common.print_debug(
                        "Chosen row out of range: row_{}".format(row), debug=debug)

                if not (Utils.Interpolate.ColumnValidate(table=table, column=column)):
                    interpolatable = False
                    Utils.Common.print_debug(
                        "Chosen column out of range: col_{}".format(column), debug=debug)

                if interpolatable:
                    interpolate_mode = InterpolateMode.SINGLE_VALUE
                    Utils.Common.print_debug(
                        "Interpolate for row_{}, col_{}".format(row, column), debug=debug)

            else:
                interpolatable = False
                Utils.Common.print_debug(
                    "Not implemented case", debug=debug)

            if interpolatable:
                Utils.Common.print_debug("Interpolatable", debug=debug)
                Utils.Common.print_debug(interpolate_mode, debug=debug)
            else:
                Utils.Common.print_debug("Un-Interpolatable", debug=debug)

            pass


class Converter:

    """
    base => yotta   :   1000000000000000000000000          1991
    base => zetta   :      1000000000000000000000          1991
    base => exa     :         1000000000000000000          1975
    base => peta    :            1000000000000000          1975
    base => tera    :               1000000000000          1960
    base => giga    :                  1000000000          1960
    base => mega    :                     1000000          1873
    base => kilo    :                        1000          1795
    base => hecto   :                         100          1795
    base => deca    :                          10          1795
    base => base    :                           1          –
    base => deci    :   0.1                                1795
    base => centi   :   0.01                               1795
    base => milli   :   0.001                              1795
    base => micro   :   0.000001                           1873
    base => nano    :   0.000000001                        1960
    base => pico    :   0.000000000001                     1960
    base => femto   :   0.000000000000001                  1964
    base => atto    :   0.000000000000000001               1964
    base => zepto   :   0.000000000000000000001            1991
    base => yocto   :   0.000000000000000000000001         1991
    """

    factor = {
        "BaseToYotta": 1000000000000000000000000,
        "BaseToZetta": 1000000000000000000000,
        "BaseToExa": 1000000000000000000,
        "BaseToPeta": 1000000000000000,
        "BaseToTera": 1000000000000,
        "BaseToGiga": 1000000000,
        "BaseToMega": 1000000,
        "BaseToKilo": 1000,
        "BaseToHecto": 100,
        "BaseToDeca": 10,
        "BaseToBase": 1,
        "BaseToDeci": 0.1,
        "BaseToCenti": 0.01,
        "BaseToMilli": 0.001,
        "BaseToMicro": 0.000001,
        "BaseToNano": 0.000000001,
        "BaseToPico": 0.000000000001,
        "BaseToFemto": 0.000000000000001,
        "BaseToAtto": 0.000000000000000001,
        "BaseToZepto": 0.000000000000000000001,
        "BaseToYocto": 0.000000000000000000000001,
    }

    m_to_foot = 3.28084

    @staticmethod
    def MeterToFoot(value):
        return value * Converter.m_to_foot

    @staticmethod
    def FootToMeter(value):
        return value / Converter.m_to_foot

    @staticmethod
    def Native(value, type):
        pre_this, pre_that = filter(None, type.split(" "))
        if pre_this.lower() == "base":
            for key in Converter.factor.keys():
                if pre_that.lower() in key.lower():
                    return value / Converter.factor[key]
            print("The native convertion may not supported yet")
        else:
            first_factor = False
            second_factor = False
            for key in Converter.factor.keys():
                if pre_this.lower() in key.lower():
                    first_factor = Converter.factor[key]
                if pre_that.lower() in key.lower():
                    second_factor = Converter.factor[key]

                if all([first_factor, second_factor]):
                    return value / (second_factor / first_factor)

        return value
