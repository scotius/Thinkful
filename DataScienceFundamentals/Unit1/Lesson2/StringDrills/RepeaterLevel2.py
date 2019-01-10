def repeater(string, n):
    # Your code goes here.
    repeatString = string * n
    outPutString = "\"" + string + "\"" +  " repeated " + str(n) + " times is: " + "\"" + repeatString + "\""
    print(outPutString)
    return outPutString
