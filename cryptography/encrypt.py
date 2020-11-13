from functions.convertions.convertDecimalToXDecimal import convertDecimalToXDecimal
from functions.variables.cryptoCharacters import cryptoCharacters

def encrypt(text, key):
    rest = ''
    crypto_text=''

    for index,letter in enumerate(text):
        if(index % 2 == 0):
            rest = ord(letter)
            if(index != len(text)-1):
                continue
            else:
            	rest = int(f'{rest}{key}')

        else:
            rest = rest - ord(letter)
            rest = int(f'{ord(letter)+rest}{key}{ord(letter)}')
        base = len(cryptoCharacters)-1
        values = convertDecimalToXDecimal(base, rest)

        for i in reversed(values):
            crypto_text +=cryptoCharacters[i]

        if(len(values)<7):
            crypto_text +=f"{'*' * (7-len(values))}"

    print("\n O texto criptografado é: ")
    print(crypto_text)
    return crypto_text