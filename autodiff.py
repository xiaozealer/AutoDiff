from numpy import sin
from Variable import *
import numpy as np
a = Variable(4, 'a')
b = Variable(3, 'b')
c = a*sin(b)
gradient = c.get_gradient()
assert gradient[a] == np.sin(b.val)
assert gradient[b] == a.val*np.cos(b.val)

# print(gradient[b])
# print(gradient[c])
# print(gradient[d])
