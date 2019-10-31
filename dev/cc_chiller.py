class Cell(object):
    def __init__(self):
        self.row = 0
        self.column = 0
        self.value = None

    @property
    def Row(self):
        return self.row

    @property
    def Column(self):
        return self.column

    @property
    def Value(self):
        return self.value

    @Value.setter
    def Value(self, value):
        self.value = value

    @property
    def ValueType(self):
        return type(self.value)


class Table(object):
    def __init__(self, data):
        self.level = 2
        self.table = {:}
        pass

    @property
    def Level(self):
        return self.level

    def Cell(self, row, column):
        pass


class Chiller(object):
    def __init__(self, table):
        self.table = table
