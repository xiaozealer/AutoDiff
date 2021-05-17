class Node:
    def __init__(self):
        pass


class Placeholder(Node):
    '''
    a placeholder node in the computational graph waits further input at 
    computation time
    Args:
        name: name of the placeholder variable
        dtype: specify the type this node holds
    '''
    count = 0

    def __init__(self, name, dtype=float):
        _g.placeholders.add(self)
        self.value = None
        self.gradient = None
        self.name = 'p{Placeholder.count}' if not name else name
        Placeholder.count += 1

    def __repr__(self):
        return 'Placeholder: {self.name}, value: {self.value}'


class Variable(Node):
    '''
    A variable node in the computational graph
    Args:
        name: default to 'var + count'
        value: a mutable value
    '''
    count = 0

    def __init__(self, value, name=None):
        _g.variables.add(self)
        self.value = value
        self.gradient = None
        self.name = 'var{self.count}' if not name else name
        count += 1

    def __repr__(self):
        return 'Variable: name: {self.name}, value:{self.value}'


class Operator(Node):
    '''
    represent the current operation
    Args:
        name: default to 'op + count'
    '''
    count = 0

    def __init__(self, name='op'):
        _g.operators.add(self)
        self.value = None
        self.inputs = []
        self.gradient = None
        self.name = name

    def __repr__(self):
        return 'Operator: name: {self.name}'


class Constant(Node):
    '''
    represent constant node in the conputation graph
    '''
    count = 0

    def __init__(self, value, name=None):
        _g.constants.add(self)
        self.value = value
        self. gradient = None
        self.name = 'Const {self.count}' if not name else name
        count += 1

    def __repr__(self):
        return 'Const: name: {self.name}, value:{self.value}'
