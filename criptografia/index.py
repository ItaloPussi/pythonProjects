from functions.generateKey import generateKey
from functions.convertions.convertDecimalToXDecimal import convertDecimalToXDecimal
from functions.convertions.convertXDecimalToDecimal import convertXDecimalToDecimal
from functions.convertions.convertLettersToNumbers import convertLettersToNumbers

from functions.variables.cryptoCharacters import cryptoCharacters

# chave = input("Digite sua chave pessoal: ")
chave = "70388261"
chave_criptografica = generateKey(chave)

# texto = input("Digite o texto a ser criptografado: ")
texto = "Bananas foram vistas na praia do m3xico"

def criptografe(texto, chave_criptografica):
    resto = ''
    texto_criptografado=''

    for index,letter in enumerate(texto):
        if(index % 2 == 0):
            resto = ord(letter)
            if(index != len(texto)-1):
                continue
        else:
            resto = (resto - ord(letter))
            resto = int(f'{ord(letter)+resto}{chave_criptografica}{ord(letter)}')
        base = len(cryptoCharacters)-1
        valores = convertDecimalToXDecimal(base, resto)

        if(len(valores)<5):
            valores.append(index)

        while(len(valores)<5):
            valores.append(0)

        if(len(valores)!=5):
            print(len(valores))
        for i in reversed(valores):
            texto_criptografado +=cryptoCharacters[i]

    print(texto_criptografado)
    return texto_criptografado

def descriptografe(texto, chave_criptografica):
    n = 5
    texto_dividido = ([texto[i:i+n] for i in range(0, len(texto), n)])
    for i in texto_dividido:
        i = i.replace("0","").strip()
        i = convertLettersToNumbers(i, cryptoCharacters)
        print(i)
        convertXDecimalToDecimal(68, i)


descriptografe(criptografe(texto, chave_criptografica), chave_criptografica)