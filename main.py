alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encrypt(key, word):
    index_char_key = 0
    result = ''
    for i in range(len(word)):
        if word[i] != ' ':
            try:
                alphabet.find(key[index_char_key])
            except:
                index_char_key = 0
            finally:
                index_char_key_alphabet = alphabet.find(key[index_char_key])
                index_char_word_alphabet = alphabet.find(word[i])
                index_char_key += 1

            sum_index = index_char_key_alphabet + index_char_word_alphabet

            if sum_index < len(alphabet):
                result += alphabet[sum_index]
            else:
                sum_index -= len(alphabet)
                result += alphabet[sum_index]
        else:
            result += ' '

    return result

def decrypt(key, word):
    index_char_key = 0
    result = ''
    for i in range(len(word)):
        if word[i] != ' ':
            try:
                alphabet.find(key[index_char_key])
            except:
                index_char_key = 0
            finally:
                index_char_key_alphabet = alphabet.find(key[index_char_key])
                index_char_word_alphabet = alphabet.find(word[i])
                index_char_key += 1

            sum_index = index_char_word_alphabet - index_char_key_alphabet - 1

            if sum_index < len(alphabet):
                result += alphabet[sum_index]
            else:
                sum_index -= len(alphabet)
                result += alphabet[sum_index]
        else:
            result += ' '

    return result

action = input('What needs to be done?\n1. Encrypt\n2. Decrypt\n')

if action == '1':
    key = input('Encryption key - ')
    word = input('Encryption Object - ')
    print('Result - ', encrypt(key, word))
elif action == '2':
    key = input('Decryption key - ')
    word = input('Decryption Object - ')
    print('Result - ', decrypt(key, word))
