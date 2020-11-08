def generateKey(userKey):
    soma = 0
    for idx,value in enumerate(userKey):
        if(idx % 2 == 0 and idx!=0):
            soma+=(idx*ord(value))
        else:
            soma+=ord(value)
    soma = str(soma % 100000)
    while len(soma) <5:
    	soma="0"+soma
    return soma