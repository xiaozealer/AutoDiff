from Operator import Operator
from collections import defaultdict


count = 0


class Variable():

    def __init__(self, value, name=None, gradient=()):
        global count
        self.val = value
        self.local_gradient = gradient
        self.name = "var"+str(count) if not name else name
        count += 1

    def __add__(self, b):
        result = self.val + b.val
        gradient = ([self, 1], [b, 1])
        return Variable(result, gradient)

    def __mul__(self, b):
        result = self.val * b.val
        gradient = ([self, b.val], [b, self.val])
        return Variable(result, gradient)

    def get_gradient(self):
        # TODO fix this function
        gradients = defaultdict(lambda: 0)

    def __str__(self) -> str:
        return '{}:{}'.format(self.name, self.val)

    def __repr__(self) -> str:
        return '{}:{}'.format(self.name, self.val)
