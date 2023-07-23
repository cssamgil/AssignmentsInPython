# this section prints the introduction to the app, explanation, and instructions
print('Welcome to the Caesar cipher app!\n')

print('The caesar cipher is one of the simplest and most \nwidely known encryption techniques, '
      'in which each \nletter of a given text is replaced by a letter \nsome fixed number of positions '
      'down the alphabet.\n')

print('in this app you will be asked to:\n -input a phrase (upper and lower case letters only,\n no spaces, punctuation'
      ' symbols, or other characters).\n -input a key (fixed number to shift the position of\n the alphabet). \n -input'
      ' choice of operation: E or D (encrypt/decrypt).')

# main function


def cipher():
    # takes phrase input and verifies there is not other characters other than letters
    phrase = input('\ninput a phrase: ')
    check = phrase.isalpha()
    while check is not True:
          print("No spaces, punctuation symbols, numbers, or other characters. please try again")
          phrase = input('input a phrase: ')
          check = phrase.isalpha()

    # takes key input and verifies there is not other characters other than fixed numbers
    key = input('input a fixed number key: ')
    check = key.isdecimal()
    while check is not True:
          print("Only fixed numbers. please try again")
          key = input('input a fixed number key: ')
          check = key.isdecimal()
    key_int = int(key)

    # takes operations input and verifies there is not other characters other that "d" or "e"
    operation = input('input "E" for encrypt, or "D" for decrypt: ')
    operation = operation.upper()
    check = 'ED'
    while len(operation) != 1 or operation not in check:
          print('"E" or "D" only, please try again')
          operation = input('input "E" for encrypt, or "D" for decrypt: ')
          operation = operation.upper()
          check = 'ED'
    # if operation to get the naming convention of the operation for later output
    operation_name = ""
    if operation == "E":
        operation_name = "Encryption"
    else:
        operation_name = "Decryption"

    # process to encrypt and decrypt the input phrase
    result = ""
    if operation == 'E':
      for i in range(len(phrase)):
       char = phrase[i]
    # Encrypt uppercase
       if char.isupper():
             result += chr((ord(char) + key_int - 65) % 26 + 65)
    # Encrypt lowercase
       else:
             result += chr((ord(char) + key_int - 97) % 26 + 97)
    elif operation == 'D':
        for i in range(len(phrase)):
            char = phrase[i]
    # Decrypt uppercase
            if char.isupper():
                result += chr((ord(char) - key_int - 65) % 26 + 65)
    # Decrypt uppercase
            else:
                result += chr((ord(char) - key_int - 97) % 26 + 97)

    # output to user
    print('\n\nOriginal phrase: ', phrase)
    print('key number: ', key)
    print('Operation: ', operation_name)
    print('\nCypher phrase: ', result)

    # ask if the user wants to try the cipher again
    x = input('\nwould you like to try again? if yes input "Y", if not "N": ')
    x = x.upper()
    if x.upper() == "Y":
        cipher()
    else:
        print("thank you!")
# initiates the program


cipher()


