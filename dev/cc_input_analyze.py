import os
import os.path as op

import csv

from cc_enum import CATALOGUE_PATH

from cc_chiller import Chiller, Table
from cc_utils import Utils, Converter


class Analyzer():

    @staticmethod
    def GetChillerDefinition():
        chiller_definition = []
        if op.isdir(CATALOGUE_PATH):
            for dirpath, dirnames, filenames in os.walk(CATALOGUE_PATH):
                for filename in filenames:
                    chiller_definition.append(CATALOGUE_PATH + filename)

        return chiller_definition

    @staticmethod
    def TableFromCSV(csv_path):
        pass

    @staticmethod
    def TableFromDefinition(definition_data):
        data = {
            "row": [],
            "column": [],
            "data": [],
        }

        return Table(data)


if __name__ == '__main__':

    chiller_definition = Analyzer.GetChillerDefinition()
    for definition_data in chiller_definition:
        print(definition_data)

    table = Analyzer.TableFromDefinition(definition_data)

    print(table)
