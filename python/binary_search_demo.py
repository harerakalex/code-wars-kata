import time

def timer(org_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = org_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} function ran in {:.3f} sec\n".format(org_func.__name__, t2))
        return res

    return wrapper


@timer
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return mid

    return -1
    
@timer
def other_way(arr, x):
    for i in arr:
        if i == x:
            return i
    return -1
       
       
arr = range(1000000000000)

print('Bin======', binary_search(arr, 10000000))
print('Other way', other_way(arr, 10000000))
