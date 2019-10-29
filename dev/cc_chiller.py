class Table(object):
    def __init__(self, data):
        pass


class Chiller(object):
    def __init__(self, table):
        self.table = table


if __name__ == '__main__':
    tb1 = Table()
    print(tb1)

    ch1 = Chiller(tb1)
    print(ch1)
