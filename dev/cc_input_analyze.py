import os
import os.path as op

from cc_enum import CATALOGUE_PATH

from cc_chiller import Chiller
from cc_utils import Utils
from cc_utils import Converter


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
    def ChillerFromDefinition():


if __name__ == "__main__":

    chiller_definition = Analyzer.GetChillerDefinition()
    print(chiller_definition)
