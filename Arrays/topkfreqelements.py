# input nums = [1,1,1,2,2,3,4], k=2
# output : [1,2]

# Goal: Count the occurrence of each element 1-3 2-2 3-1 4-1

# Logic: Bucket Sort
# 1. Freq = Same size as that of an input array 
# 2. Count = hashmap 
# 3. Count the occurrence of each element in an array by going through nums and adding the occurrences to count[n].
# 4. Going through each key: value pair in the hashmap(count). Append the value of n to the occurence of c. 
# i.e n appears c number of times. n= 1 appears c=3 number of times.
# 5. Res = should return top k elements
# 6. Going from last index to the first in descending order. Append the element to res. 
# 7. Once it reaches k times we return the rest


def func(nums):
    freq = [[] for i in range(n + 1)]
    count = {}
    
    # Count the frequency of each word
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    # Group words by their frequency
    for word, freq_count in count.items():
        freq[freq_count].append(word)
    
    result = []
    # Traverse freq list in reverse order to get top k frequent words
    for i in range(len(freq)-1, 0, -1):
            res += freq[I]
            if len(result) >= k:
                return result[:k]


