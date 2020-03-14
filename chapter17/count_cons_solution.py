"""
Object Count Solution
"""


class Counter(object):
    count = 0

    def __init__(self, value):
        self.value = value
        Counter.count += 1

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def get_count(self):
        return Counter.count


instance_a = Counter([5, 10, 20])
for _, number_list in enumerate(instance_a.get_value()):
    print("value of object: {}".format(number_list))
    print("Instance Count: {}".format(instance_a.get_count()))
