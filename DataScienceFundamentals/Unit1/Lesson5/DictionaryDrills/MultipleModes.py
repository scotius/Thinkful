def modes(data):
    counts = {}
    inputs = data
    countList = []
    modeList = []
    outputs = []
    hasModes = False
    modeKey = 0
    for input in inputs:
        #if input index already exists increase value by one
        #otherwise create index in dictionary and set its initial value to 1
        if input in counts.keys():
            counts[input] +=1
        else:
            counts[input] = 1

    for item in counts.items():
        countList.append(item[1])

    for count in countList:
        if len(countList) == 1:
            hasModes = False
        #if the number of each item is the same, there is no mode
        elif count != countList[0]:
            hasModes = True
            modeKey = max(countList)
            for item in counts.items():
                if item[1] == modeKey:
                    modeList.append(item[0])
    if hasModes:
        outputs = sorted(list(set(modeList)))
        return outputs
    else:
        return []
