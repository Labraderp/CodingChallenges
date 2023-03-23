def longest_repetition(chars):
    #edge case: empty list
    if len(chars) == 0:
        return ('', 0)
    
    #edge case: one element
    if len(chars) == 1:
        return (char[0], 1)
    
    #edge case: two elements
    if len(chars) == 2:
        if chars[0] == chars[1]:
            return (chars[0], 2)
        else:
            return (chars[0], 1)
    
    
    longest = ['', 0]   #values to return
    memory = chars[0]   #saving first index
    increment = 1       #increment at first index
    print('target array: ', chars)
    
    for char in chars[1:]:
        #if current char == last char, increment counter
        if char == memory:
            increment += 1
        
        else:
            if increment > longest[1]:
                longest[0] = memory
                longest[1] = increment
            memory = char
            increment = 1
    
    #check based on last index value
    if increment > longest[1]:
            longest[0] = memory
            longest[1] = increment
    return (longest[0], longest[1])