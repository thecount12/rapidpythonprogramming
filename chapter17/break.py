"""
Break Encapsulation
"""


class BreakEncapsulation(object):
    """break encap"""
    def set_value(self, value):
        try:
            value = int(value)
        except:
            return
        self.value = value

    def get_value(self):
        return self.value

    def increment_value(self):
        self.value = self.value + 1


i = BreakEncapsulation()
i.set_value(42)
print(i.get_value())
i.value = 'hi'
print(i.get_value())
print(i.increment_value())
