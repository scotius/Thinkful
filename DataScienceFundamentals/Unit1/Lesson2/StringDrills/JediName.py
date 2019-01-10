def greet_jedi(first, last):
    jediName = last[0:3].capitalize() + first[0:2].capitalize()
    outPutString = 'Greetings, master ' + jediName
    print(outPutString)
    return outPutString
