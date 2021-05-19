

from Variable import Variable


class Operator:
    def __init__(self):
        pass

    def add(self, a, b):
        '''
        takes two operators and add them together
        '''
        result = a + b
        gradient = [(a, 1), (b, 1)]
        return Variable(result, gradient)

    def multiply(self, a, b):
        result = a * b
        gradient = [(a, b.val), (b, a.val)]
        return Variable(result, gradient)
