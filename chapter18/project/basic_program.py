"""
basic program to test
"""


class Basic(object):

    def __init__(self, num_1, num_2):
        self.number_1 = num_1
        self.number_2 = num_2

    def multiply(self):
        return self.number_1 * self.number_2

    def add(self):
        return self.number_2 + self.number_1

    def report(self):
        return "hello world"

    def combine(self):
        data = self.add()
        comb = self.add() + self.multiply()
        my_string = (f"data addtion: {data}")
        my_list = [data, comb, my_string]
        return tuple(my_list)


if __name__ == "__main__":
    foo = Basic(2, 3)
    print(foo.multiply())
    print(foo.add())
    print(foo.report())
    print(foo.combine())
