from cc_enum import DefinitionRowType, TemperatureType, BuiltinRunOptions, BuiltinInputOptions
from cc_chiller import Chiller, Table

from cc_utils import Utils, Converter


if __name__ == '__main__':

    if TemperatureType.IS_GOOD:
        print("hi")

    if TemperatureType.IS_TOOHIGH.value == 1:
        print("hi")

    table_data = {
        "row_header": [5, 7, 11, 19],
        "column_header": [35, 40, 45, 50],
        "data": [
            [0, 0, 713.44, 634.9616],
            [728, 640.64, 544.544, 533.65312],
            [698.88, 670.9248, 590.413824, 507.7558886],
            [670.9248, 644.087808, 547.4746368, 498.2019195],
        ],
    }

    tb1 = Table(table_data)
    print(tb1)

    for row in tb1.table:
        print(row)
        print(row.index)
        print(row.header)
        for cell in row.cells:
            print(cell)
            print(cell.row)
            print(cell.col)
            print(cell.value)

    ch1 = Chiller(tb1)
    print(ch1)

    print(Converter.Native(100, "bAse miLli"))
    print(Converter.Native(100, "bAse kilo"))
    print(Converter.Native(100, "deci kilo"))
    print(Converter.Native(100, " kilo deci"))

    print(tb1.Level)

    Utils.Interpolate.TableValidate(table=tb1, row=9)
    Utils.Interpolate.TableValidate(table=tb1, column=37)
    Utils.Interpolate.TableValidate(table=tb1, row=9, column=37)

    Utils.Interpolate.TableValidate(table=tb1, row=2)
    Utils.Interpolate.TableValidate(table=tb1, column=57)
    Utils.Interpolate.TableValidate(table=tb1, row=2, column=37)
    Utils.Interpolate.TableValidate(table=tb1, row=9, column=57)
    Utils.Interpolate.TableValidate(table=tb1, row=2, column=57)
