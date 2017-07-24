# -*- coding: utf-8 -*-
"""
@author: rajat
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''

    return aTup[::2] # Slicing the tuple for odd indices
                     # Note: aTup[1::2] --> this gives even tuples

a = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(a))
