"""
Constructor object counting
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


instance_a = Counter(5)
instance_b = Counter(10)
instance_c = Counter(20)

for object_value in (instance_a, instance_b, instance_c):
    print("value of object: {}".format(object_value.get_value()))
    print("Instance Count: {}".format(object_value.get_count()))
