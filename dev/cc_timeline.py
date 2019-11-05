from cc_utils import Utils, Converter

debug = True
# debug = False


class Timeline():
    def __init__(self, start=0, count=8760, step=1):
        self.start = start
        self.present = self.start
        self.count = count
        self.step = step

    @property
    def Start(self):
        return self.start

    @property
    def End(self):
        return self.count

    @property
    def Present(self):
        return self.present

    @property
    def Past(self):
        if self.present == 0:
            return self.count
        else:
            return self.present - self.step

    @property
    def Future(self):
        if self.present == self.count:
            return 0
        else:
            return self.present + 1

    # @property
    # def LabelOfPresent(self):
    #     return self.LabelOfState(self.Present)
    #
    # @property
    # def LabelOfPast(self):
    #     return self.LabelOfState(self.Past)
    #
    # @property
    # def LabelOfFuture(self):
    #     return self.LabelOfState(self.Future)
    #
    # def LabelOfState(self, state):
    #     if state > self.max:
    #         return self.label[0]
    #     elif state < 0:
    #         return self.label[self.max]
    #     else:
    #         return self.label[state]

    def Next(self):
        if self.present == self.count:
            self.present = 0
        else:
            self.present += 1

        Utils.Common.print_debug(
            "Go to next step {}".format(self.present), debug=debug)

        return True

    def Back(self):
        if self.present == 0:
            self.present = self.count
        else:
            self.present -= 1

        Utils.Common.print_debug(
            "Go to previous step {}".format(self.present), debug=debug)

        return True

    @classmethod
    def TimelineFromLoad(cls, load):
        timeline = cls(len(load.load))
        timeline.label = load.load
        return timeline


if __name__ == "__main__":

    timeline = Timeline(count=8760)

    print(timeline)
    print(timeline.Present)
    print(timeline.Next())
    print(timeline.Present)
