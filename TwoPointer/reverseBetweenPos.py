#You receive a vector/ array and 2 numbers, eg 2 and 5. Between those 2 positions in the vector (2 and 5) you have to reverse the order of the elements.
def func(a,l,k):
    
    k = k-1
    while l < k:
        a[l],a[k] = a[k],a[l]
        l+=1
        k-=1
        
    return a
        
    
a = [1, 2, 3, 4, 5, 6]
l=2
k = 4
print(func(a,l,k))
                
