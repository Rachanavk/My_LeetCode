def func(a, k, n):
    freq = [[] for i in range(n + 1)]
    count = {}
    
    # Count the frequency of each word
    for word in a:
        count[word] = 1 + count.get(word, 0)
    
    # Group words by their frequency
    for word, freq_count in count.items():
        freq[freq_count].append(word)
    
    result = []
    # Traverse freq list in reverse order to get top k frequent words
    for i in range(n, 0, -1):
        if freq[i]:
            result.extend(sorted(freq[i]))
            if len(result) >= k:
                return result[:k]

a = ["i", "love", "leetcode", "i", "love", "coding"]
n = len(a)
k = 2
print(func(a, k, n))
