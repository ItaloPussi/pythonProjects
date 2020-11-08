from functions.utils.generateKey import generateKey
from functions.utils.bruteForceBarrier import bruteForceBarrier
from criptografe import criptografe
from descriptografe import descriptografe

from playsound import playsound

def collectInformation(attempt, barrier):
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
            attempt+=1
            if(attempt >= 3):
                print("Alarme disparado! ")
                playsound("alarmy.mp3")
                pass
            bruteForceBarrier(barrier)
            barrier *= 2.5
            if(barrier>86400):
                barrier = 86400
        else:
            attempt=0
            barrier=10
    collectInformation(attempt, barrier)

collectInformation(0,10)