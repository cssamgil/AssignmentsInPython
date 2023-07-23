# Carlos Sanchez COP4045 Assignment 3

In this assignment we were asked to create a Caesar cypher app that will take a line from a .txt file and give the option to the user to encrypt or decrypt it. after execute, the program will create a new .txt fiel name "file_name"_dec.txt if decrypts or "file_name"_enc.txt if encrypts.

I divide this project in 4 parts:

##### 1. check & read:  

for this part I did a while loop to look for the .txt file and after the loop it will read the line in using "f.readline". if not .txt file was found or the user typed and incorrect file name, the loop will ask the user to try again. 

        file_name = input("\nPlease Enter the .txt file name: ")
        while os.path.isfile(file_name) is False:
        file_name = input("File doesn't exists, try again: ")
        print("File exists")
        # opens and reads file
        f = open(file_name, "r")
        file_name2 = file_name.split(".")[0]
        read = f.readline().rstrip('\n')
   
##### 2. Operation: 

for this part we were given a fixed key, so there was not need to ask the user for it. However, we need to ask for the type of operation (encrypt or decrypt). I used my A2 and used the same while loop to assure E or D was the input from the user.

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

##### 3. decrypt() &  encrypt()

In this project we dive into the use of funtions, so I used my past assignment and created a decrypt() and  encrypt() funtions. the program will call them depending if the input from the user is "D" or "E" with a If statement.

- Encrypt():


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

- Decrypt():


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

- Call:


        # calls encrypt or decrypt functions
        if operation == "E":
            encrypt()
        else:
            decrypt()

##### 4. Result & Loop

Result: This was not the same as assignment 2. This time for result the program will create a new .txt fiel name "file_name"_dec.txt if decrypts or "file_name"_enc.txt if encrypts and will have the encrypted or decrypted sentence or word inside of the file.

- For the naming convencion I use a split:
```python
file_name2 = file_name.split(".")[0]
```
- To create a new file I placed the following code inside decrypt() and  encrypt() funtions:

```python
    # creates a new .txt file adding _enc at the end of the original file's name
     f = open(file_name2 + "_enc.txt", "x")
     f.write(result)
     print('\nEncrypted text: ', result)
     output()
    
    # creates a new .txt file adding _dec at the end of the original file's name
     f = open(file_name2 + "_dec.txt", "x")
     f.write(result)
     print('\nEncrypted text: ', result)
     output()
```

- I  keep the same output function to aslo print in the terminal as the last assingment:

```python
    def output():
        print('Original text: ', read)
        print('key number: ', key)
        print('Operation: ', operation)
```

Try again Loop: I used the same call funtion as assigment two to create a loop, that if the user want to try again it will only call the finction again restarting the app

```python
    # ask if the user wants to try the cipher again
    x = input('\nwould you like to try again? if yes input "Y", if not "N": ')
    x = x.upper()
    if x.upper() == "Y":
        cipher()
    else:
        print("thank you!")
```
