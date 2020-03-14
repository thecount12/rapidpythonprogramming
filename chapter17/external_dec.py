"""
External static class
"""


class Counter(object):
    count = 0

    def __init__(self, value):
        # self.value = value
        self.value = self.my_filter(value)
        Counter.count += 1

    @staticmethod
    def my_filter(my_value):
        ar = []
        for x in iter(my_value):
            if not isinstance(x, int):
                ar.append(0)
            else:
                ar.append(x)
        return ar

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    @classmethod
    def get_count(cls):
        return cls.count


instance_a = Counter([5, 10, 20, 'hello'])
for _, number_list in enumerate(instance_a.get_value()):
    print("value of object: {}".format(number_list))
    print("Instance Count: {}".format(instance_a.get_count()))
print(Counter.get_count())
