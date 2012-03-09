'''
@authors: Richard B. Johnson
'''
import sys
import inspect

global active
active = True

def notify(str):
    if active: print "-> %s"%(str)

def error(str):
    print "Error: %s"%(str)

# Courtesy of Hal Daume III
def raiseNotDefined():
    error("Method not implemented: %s" % inspect.stack()[1][3])
    sys.exit(1)
