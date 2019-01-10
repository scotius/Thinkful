def area_code(text):
    startIndex = text.find('(')
    endIndex = text.find(')')
    outputString = text[startIndex + 1 :endIndex]
    return (outputString)
