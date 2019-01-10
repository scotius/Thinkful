def longest(words):
    #Initially make the first word in the array the longest
    longestWord = len(words[0])
    #Iterate through the string array starting with the second word
    #If word length is longer than longestWord
    #longestWord is assigned that value
    for index in range (1,(len(words))):
        if len(words[index]) > longestWord:
            longestWord = len(words[index])
    return longestWord
