import numpy as np


class Graph():
    '''
    This class is used to reprsent computational graph for AutoDiff
    Each graph consist of a set of 
    1. Operators
    2. Variables
    3. Constants
    4. Placeholders
    '''

    def __init__(self):
        self.operators = set()
        self.variable = set()
        self.constants = set()
        self.placeholders = set()
