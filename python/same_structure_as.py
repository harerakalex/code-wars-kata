'''
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''

import numpy as np

def same_structure_as(original,other):
    if type(original) != type(other):
        return False
    if len(original) != len(other):
        return False
    
    original_shapes = [array_shape(x) for x in original]
    other_shapes = [array_shape(x) for x in other]
    
    if np.array_equal(original_shapes, other_shapes):
        return True
    return False

def array_shape(arr):
    return np.array(arr).shape