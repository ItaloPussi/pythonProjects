from functions.utils.generateKey import generateKey
from functions.utils.bruteForceBarrier import bruteForceBarrier
from encrypt import encrypt
from decrypt import decrypt

from playsound import playsound

def collectInformation(attempt, barrier):
    option = ''
    while (option!="c" and option!="d"):
        option = input("Deseja [C]riptografar ou [D]escriptografar? ").lower()

    keyNotFormated = input("Digite sua chave de acesso: ")
    key = generateKey(keyNotFormated)

    if(option=="c"):
        text = input("Digite o texto a ser criptografado: ")
        encrypt(text, key)
    else:
        text = input("Digite o texto a ser descriptografado: ")
        response = decrypt(text, key)

        # Brute force? Here no!
        if(not response):
            attempt+=1

            # Let's make some noise
            if(attempt >= 3):
                print("Alarme disparado! ")
                playsound("alarmy.mp3")
                pass

            # And a little wait
            bruteForceBarrier(barrier)
            barrier *= 2.5

            # The maximum time will be 1 day
            if(barrier>86400):
                barrier = 86400

        # Decrypt was successful? Reset barrier and attempt
        else:
            attempt=0
            barrier=10
    collectInformation(attempt, barrier)

collectInformation(0,10)