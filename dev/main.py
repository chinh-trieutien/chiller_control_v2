from cc_calculator import Calculator
from cc_calculator import Input, RunOptions

if __name__ == '__main__':

    calc = Calculator()

    runOpts = RunOptions()
    inputs = Input()

    calc.RunOptions = runOpts
    calc.Input = inputs

    calc.Run()
