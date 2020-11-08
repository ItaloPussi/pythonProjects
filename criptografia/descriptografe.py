from functions.convertions.convertXDecimalToDecimal import convertXDecimalToDecimal
from functions.convertions.convertLettersToNumbers import convertLettersToNumbers
from functions.variables.cryptoCharacters import cryptoCharacters

def descriptografe(texto, chave_criptografica):
    n = 7
    texto_dividido = ([texto[i:i+n] for i in range(0, len(texto), n)])
    textoy = ''
    for i in texto_dividido:
        i = i.replace("*","").strip()
        i = convertLettersToNumbers(i, cryptoCharacters)
        i = i.split(",")
        i.remove('')

        i = convertXDecimalToDecimal(68, i)
        i = str(i).split(str(chave_criptografica))

        try:
            for h in i:
                if h == '':
                    continue
                textoy+=(chr(int(h)))
        except ValueError:
            print("Impossível descriptografar a mensagem, aguarde um momento...")
            return False
    print("\n O texto descriptografado é: ")
    print(textoy)
    return True