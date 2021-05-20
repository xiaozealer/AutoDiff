from collections import defaultdict
import numpy as np

count = 0


class Variable:

    def __init__(self, value, name=None, gradient=()):
        global count
        self.val = value
        self.local_gradient = gradient
        self.name = "var"+str(count) if not name else name
        count += 1

    def __add__(self, b):
        result = self.val + b.val
        gradient = ([self, 1], [b, 1])
        print(gradient)
        return Variable(result, gradient=gradient)

    def __mul__(self, b):
        result = self.val * b.val
        gradient = ([self, b.val], [b, self.val])
        print(gradient)
        return Variable(result, gradient=gradient)

    def __neg__(self):
        result = -1 * self.val
        gradient = ([self, -1])
        return Variable(result, gradient=gradient)

    def __sub__(self, b):
        result = self.val - b.val
        gradient = ([self, 1], [b, -1])
        print(gradient)
        return Variable(result, gradient=gradient)

    def __truediv__(self, b):
        result = self.val / b.val
        gradient = ([self, 1/b.val], [b, -self.val * (b.val**(-2))])
        print(gradient)
        return Variable(result, gradient=gradient)

    def __repr__(self) -> str:
        return '{}:{}'.format(self.name, self.val)

    def get_gradient(self):
        gradients = defaultdict(lambda: 0)
        self.compute_gradient(gradients, 1)
        return gradients

    def compute_gradient(self, gradients, last_gradient):
        for var, derative in self.local_gradient:  # empty to be fixed
            local_grad = last_gradient * derative
            gradients[var] += local_grad
            var.compute_gradient(gradients, local_grad)
