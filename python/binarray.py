def binarray(s)->int:
    max_len = 0
    for start in range(len(s)):
        zeroes = 0
        ones = 0
        for end in range(start, len(s)):
            if s[end] == 0:
                zeroes+=1
            else:
                ones+=1
            if zeroes == ones:
                max_len = max(max_len, end - start + 1)
    
    return max_len
