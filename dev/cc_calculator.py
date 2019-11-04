import os
import os.path as op

from cc_enum import root
from cc_enum import CHILLER_PATH

from cc_chiller import Chiller
from cc_utils import Utils

debug = True
# debug = False


class Calculator():
    def __init__(self):
        Utils.Common.print_debug("init Calculator object", debug=debug)
        self.opts = None
        self.inputs = None
        Utils.Common.print_debug(
            "init Calculator object successful", debug=debug)

    @property
    def RunOptions(self):
        Utils.Common.print_debug("Get RunOptions", debug=debug)
        return self.opts

    @RunOptions.setter
    def RunOptions(self, value):
        Utils.Common.print_debug("Set RunOptions", debug=debug)
        if isinstance(value, RunOptions):
            self.opts = value
            self.ExtractRunOptions()
            Utils.Common.print_debug("Set RunOptions Successful", debug=debug)
        else:
            Utils.Common.print_debug(
                "Set RunOptions Un-successful, Use RunOptions object only", debug=debug)
        pass

    @property
    def Input(self):
        Utils.Common.print_debug("Get Input", debug=debug)
        return self.inputs

    @Input.setter
    def Input(self, value):
        Utils.Common.print_debug("Set Input", debug=debug)
        if isinstance(value, Input):
            self.inputs = value
            self.ExtractInput()
            Utils.Common.print_debug("Set Input Successful", debug=debug)
        else:
            Utils.Common.print_debug(
                "Set Input Un-successful, Use Input object only", debug=debug)
        pass

    def ExtractRunOptions(self):
        Utils.Common.print_debug("Extract data from RunOptions", debug=debug)
        pass
        Utils.Common.print_debug(
            "Extract data from RunOptions successful", debug=debug)

    def ExtractInput(self):
        Utils.Common.print_debug("Extract data from Input", debug=debug)
        pass
        Utils.Common.print_debug(
            "Extract data from Input successful", debug=debug)

    def Run(self):
        Utils.Common.print_debug("Run Calculation", debug=debug)
        pass


class RunOptions():

    def __init__(self):
        Utils.Common.print_debug("init RunOptions object", debug=debug)
        self.opts = []
        Utils.Common.print_debug(
            "init RunOptions object successful", debug=debug)


class Input(object):

    def __init__(self):
        Utils.Common.print_debug("init Input object", debug=debug)
        pass
        Utils.Common.print_debug("init Input object successful", debug=debug)


if __name__ == '__main__':

    calc = Calculator()

    runOpts = RunOptions()
    inputs = Input()

    calc.RunOptions = runOpts
    calc.Input = inputs

    calc.Run()
