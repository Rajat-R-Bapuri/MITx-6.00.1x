import math

def polysum(n, s):
    '''
    n: number of sides of polygon
    s: length of each side
    
    returns: sum of area and sqaure of perimeter
    '''
    area = (0.25 * n * s ** 2) / (math.tan(math.pi/n))
    perimeter = n * s
    return round(area + perimeter ** 2, 4)
