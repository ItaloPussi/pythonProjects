from functions.convertions.convertDecimalToXDecimal import convertDecimalToXDecimal
from functions.variables.cryptoCharacters import cryptoCharacters

def criptografe(texto, chave_criptografica):
    resto = ''
    texto_criptografado=''

    for index,letter in enumerate(texto):
        if(index % 2 == 0):
            resto = ord(letter)
            if(index != len(texto)-1):
                continue
        else:
            resto = resto - ord(letter)
            resto = int(f'{ord(letter)+resto}{chave_criptografica}{ord(letter)}')
        base = len(cryptoCharacters)-1

        valores = convertDecimalToXDecimal(base, resto)
        for i in reversed(valores):
            texto_criptografado +=cryptoCharacters[i]

        if(len(valores)<5):
            texto_criptografado +=f"{'*' * (5-len(valores))}"

    print("\n O texto criptografado é: ")
    print(texto_criptografado)
    return texto_criptografado