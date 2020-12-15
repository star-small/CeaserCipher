import random
import os
import sys
os.system('figlet -c C a e s a r Cipher ')



def ciphering(word):
    bias = sum(list(map(lambda x: int(x), [i for i in passwd])))
    cipher_word = []

    for i in range(len(word)):
        cipher = ord(word[i]) + bias + i * i
        cipher_word.append(chr(cipher))
    return ''.join(cipher_word)


def deciphering(word):
    bias = sum(list(map(lambda x: int(x), [i for i in passwd])))
    decipher_word = []
    for i in range(len(word)):
        cipher = ord(word[i])
        decipher = chr((cipher - bias) - i * i)

        decipher_word.append(decipher)


    return ''.join(decipher_word)



iter = True
try:
    while iter:
        choose = input("1.Шифровать\n2.Расшифровать\n")
        try:
            try:
                if choose == "1":
                    print("\n\033[33mВнимание! шифруемый текст не должен содержать переноса строки!\033[0m\n")
                    passwd = str(random.randint(100, 99999))
                    print("Ваш пароль расшифровки - \033[32m{}\033[0m, не потеряйте его!".format(passwd))
                    road = sys.argv[-1]

                    with open(road, 'r') as content_file:
                        content = content_file.read()
                    with open(ciphering(road), 'w') as handler:
                        handler.write(ciphering(content))
                    print('Done.')
                    os.system('pwd {}'.format(ciphering(road)))
                    print(ciphering(road), '\t <------ filname')
                    iter = False
                elif choose == "2":
                    road = sys.argv[-1]
                    passwd = input("Введите пароль расшифровки: ")


                    with open(road, 'r') as content_file:
                        content = content_file.read()
                    with open(deciphering(road), 'w') as handler:
                        handler.write(deciphering(content))
                    print('Done.')
                    iter = False
                else:
                    print("\nВведите корректное значение\n")
            except ValueError:
                print("Не поддерживаемый формат :(")

        except FileNotFoundError:
            print("\n\033[33mФайл не найден\033[0m\n")
except KeyboardInterrupt:
    print("\nЗавершение программы...")
