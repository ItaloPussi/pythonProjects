from functions.convertions.convertXDecimalToDecimal import convertXDecimalToDecimal
from functions.convertions.getIndexesOfValuesInArray import getIndexesOfValuesInArray
from functions.variables.cryptoCharacters import cryptoCharacters

def decrypt(text, key):
    n = 7

    # Divide the text by n characters blocks each
    divided_text = ([text[i:i+n] for i in range(0, len(text), n)])
    decrypted_text = ''

    for block in divided_text:
        block = block.replace("*","").strip()
        block = getIndexesOfValuesInArray(block, cryptoCharacters)
        block = block.split(",")
        block.remove('')

        block = convertXDecimalToDecimal(68, block)
        block = str(block).split(str(key))

        try:
            for value in block:
                if value == '':
                    continue
                decrypted_text+=(chr(int(value)))
        except OverflowError:
            print("Impossível descriptografar a mensagem, aguarde um momento...")
            return False
    print("\n O texto descriptografado é: ")
    print(decrypted_text)
    return True