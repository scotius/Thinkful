def user_contacts(data):
    name = ''
    zip = ''
    outputDict = {}
    for datum in data:
        if len(datum) < 2:
           name = datum[0]
           zip = None
           outputDict[name] = zip
        else:
           name = datum[0]
           zip = datum[1]
           outputDict[name] = zip
    return outputDict
