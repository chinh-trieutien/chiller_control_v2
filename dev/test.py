from cc_enum import DefinitionRowType, TemperatureType, BuiltinRunOptions, BuiltinInputOptions
from cc_chiller import Chiller, Table

from cc_utils import Utils, Converter


if __name__ == '__main__':

    if TemperatureType.IS_GOOD:
        print("hi")

    if TemperatureType.IS_TOOHIGH.value == 1:
        print("hi")

    table_data = []

    tb1 = Table(table_data)
    print(tb1)

    ch1 = Chiller(tb1)
    print(ch1)

    print(Converter.Native(100, "bAse miLli"))
    print(Converter.Native(100, "bAse kilo"))
    print(Converter.Native(100, "deci kilo"))
    print(Converter.Native(100, " kilo deci"))

    print(tb1.Level)

    Utils.Interpolate(table=tb1, row=9, column=37)
