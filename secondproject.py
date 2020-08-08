from firstproject import Chandra


class Child(Chandra):

    def __init__(self):
        Chandra.__init__(self, 2, 3)

    def sum_of_var(self):
        return self.sum()


ch=Child()
print(ch.sum_of_var())




