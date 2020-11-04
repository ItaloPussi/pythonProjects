import time

from functions.generateKey import generateKey
from functions.convertions.convertDecimalToXDecimal import convertDecimalToXDecimal
from functions.convertions.convertXDecimalToDecimal import convertXDecimalToDecimal
from functions.convertions.convertLettersToNumbers import convertLettersToNumbers

from functions.variables.cryptoCharacters import cryptoCharacters

def bruteForceBarrier(barrier):
    time.sleep(barrier)

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

def descriptografe(texto, chave_criptografica):
    n = 5
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
                textoy+=(chr(int(h)))
        except ValueError:
            print("Impossível descriptografar a mensagem, aguarde um momento...")
            return False
    print("\n O texto descriptografado é: ")
    print(textoy)
    return True


def collectInformation(barrier):
    opcao = ''
    while (opcao!="c" and opcao!="d"):
        opcao = input("Deseja [C]riptografar ou [D]escriptografar? ").lower()
    if(opcao=="c"):
        chave = input("Digite sua chave de acesso: ")
        chave_criptografica = generateKey(chave)
        texto = input("Digite o texto a ser criptografado: ")
        criptografe(texto, chave_criptografica)
    else:
        chave = input("Digite sua chave de acesso: ")
        chave_criptografica = generateKey(chave)
        texto = input("Digite o texto a ser descriptografado: ")
        response = descriptografe(texto, chave_criptografica)
        if(not response):
            bruteForceBarrier(barrier)
            barrier = barrier * 2.5
            if(barrier>86400):
                barrier = 86400
            collectInformation(barrier)

collectInformation(10)