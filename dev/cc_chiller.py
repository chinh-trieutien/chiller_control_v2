class Cell(object):
    def __init__(self):
        self.row = 0
        self.col = 0
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

    @staticmethod
    def Null(row, col):
        null_cell = Cell()
        null_cell.row = row
        null_cell.col = col
        null_cell.value = None
        return null_cell


class Row(object):
    def __init__(self):
        self.index = 0
        self.header = 0
        self.count = 0
        self.cells = []

    def AddCell(self, cell):
        self.cells.append(cell)
        self.count = len(self.cells)


class Column(object):
    pass


class Table(object):
    def __init__(self, data):
        self.level = 2
        self.data = data
        self.table = []
        self.row_count = 0
        self.col_count = 0
        self.TableFromData()

    @property
    def Level(self):
        return self.level

    def TableFromData(self):

        row_indx = 0
        for row_data in self.data["data"]:
            row = Row()
            row.header = self.data["row_header"][row_indx]
            col_indx = 0
            for item in row_data:
                cell = Cell()

                cell.row = row_indx
                cell.col = col_indx
                cell.value = item

                col_indx += 1

                row.AddCell(cell)

            row_indx += 1
            self.AddRow(row)

        row_len = 0
        for row in self.table:
            if row.count > row_len:
                row_len = row.count

        for row in self.table:
            if row.count < row_len:
                while row.count < row_len:
                    row.AddCell(Cell.Null(row.index, row.count + 1))

    def AddRow(self, row):
        self.table

        row.index = self.row_count
        row.header = self.data

        self.row_count += 1


class Chiller(object):
    def __init__(self, table):
        self.table = table
