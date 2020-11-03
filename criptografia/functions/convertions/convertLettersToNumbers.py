def convertLettersToNumbers(thing, cryptoCharacters):
    converted = ''
    for i in reversed(thing):
        converted+=str(cryptoCharacters.index(i))+','
    return converted
            