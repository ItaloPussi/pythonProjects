def generateKey(userKey):
    valueSum = 0
    for idx,value in enumerate(userKey):

        # It's even? If so multiply the index by ascii code and then put on sum variable
        if(idx % 2 == 0 and idx!=0):
            valueSum+=(idx*ord(value))
        # If not, just put the ascii code in the sum variable
        else:
            valueSum+=ord(value)

    valueSum = str(valueSum % 100000)

    # The key always will have five digits
    while len(valueSum) <5:
    	valueSum="0"+valueSum

    return valueSum