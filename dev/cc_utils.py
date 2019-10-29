import time
import datetime

from copy import deepcopy


class Utils(object):

    @staticmethod
    def print_debug(msg, debug=False, debug_level=3):
        if debug:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg)
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


if __name__ == "__main__":

    print(Converter.Native(100, "bAse miLli"))
    print(Converter.Native(100, "bAse kilo"))
    print(Converter.Native(100, "deci kilo"))
    print(Converter.Native(100, " kilo deci"))
