
#Given an unsorted array, write a function which will accept the array and return the minimum difference between any pair.
def func(a):
    a.sort()
    l = 0
    r = 1
    res = a[0]
    diff = 0
    while r < len(a):
        diff = a[r] - a[l]
        res = min(res,diff)
        l+=1
        r+=1
    return res
a = [1, 5, 3, 19, 18, 25]
print(func(a))
                
    
