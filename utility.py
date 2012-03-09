'''
@authors: Richard B. Johnson
'''
from random import Random
import debug

global random
random = Random()

def col(str):
    return "%-10s"%("%s:"%(str))

