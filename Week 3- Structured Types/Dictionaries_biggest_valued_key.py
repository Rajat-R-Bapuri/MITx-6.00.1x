# -*- coding: utf-8 -*-
"""
@author: rajat
"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maximum = 0
    result = 0
    for i in aDict.keys():
        if len(aDict[i]) > maximum:
            result = i
            maximum = len(aDict[i])
    return result
            
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
