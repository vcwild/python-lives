from functools import reduce
from operator import add


float_list = [1.22, 1.13, 4.25]

response = reduce(lambda termo, acc: acc + termo, float_list)
