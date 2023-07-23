import os.path

# this section prints the introduction to the app, explanation, and instructions
print('Welcome to the Caesar cipher app!\n')

print('The caesar cipher is one of the simplest and most \nwidely known encryption techniques, '
      'in which each \nletter of a given text is replaced by a letter \nsome fixed number of positions '
      'down the alphabet.\n')

print('in this app you will be asked to:\n -Input filename (from which the plaintext or\n cypher-text will be read)\n '
      '-Input the choice of operation (E/D, for encrypt/decrypt)\n -Shift key number is 3.')

# main function


def cipher():
    # loop that checks for file.
    file_name = input("\nPlease Enter the .txt file name: ")
    while os.path.isfile(file_name) is False:
        file_name = input("File doesn't exists, try again: ")
    print("File exists")
    # opens and reads file
    f = open(file_name, "r")
    file_name2 = file_name.split(".")[0]
    read = f.readline().rstrip('\n')

    # fixed key
    key = 3
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


    def output():
        print('Original text: ', read)
        print('key number: ', key)
        print('Operation: ', operation)

    # process to encrypts file's text
    def encrypt():
        result = ""
        for i in range(len(read)):
            char = read[i]
            # Encrypt uppercase
            if char.isupper():
                result += chr((ord(char) + key_int - 65) % 26 + 65)
            # Encrypt lowercase
            elif char.islower():
                result += chr((ord(char) + key_int - 97) % 26 + 97)
            # spaces and special characters are not being change
            else:
                result += char
        # creates a new .txt file adding _dec at the end of the original file's name
        f = open(file_name2 + "_enc.txt", "x")
        f.write(result)
        print('\nEncrypted text: ', result)
        output()

    # process to decrypts file's text 

    def decrypt():
        result = ""
        for i in range(len(read)):
            char = read[i]
            # Decrypt uppercase
            if char.isupper():
                result += chr((ord(char) - key_int - 65) % 26 + 65)
            # Decrypt uppercase
            elif char.islower():
                result += chr((ord(char) - key_int - 97) % 26 + 97)
            # spaces and special characters are not being change
            else:
                result += char
        # creates a new .txt file adding _dec at the end of the original file's name
        f = open(file_name2 + "_dec.txt", "x")
        f.write(result)
        print('\nEncrypted text: ', result)
        output()

    # calls encrypt or decrypt functions
    if operation == "E":
        encrypt()
    else:
        decrypt()

    # ask if the user wants to try the cipher again
    x = input('\nwould you like to try again? if yes input "Y", if not "N": ')
    x = x.upper()
    if x.upper() == "Y":
        cipher()
    else:
        print("thank you!")


cipher()