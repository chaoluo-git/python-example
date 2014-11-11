__author__ = 'lch'

class Members:
    """
     test __getitem__
    """
    def __init__(self, value):
        self.value = [value + '1', value + '2']

    def __getitem__(self, item):
        print self.value[item]

m = Members('tom')
m[1]
