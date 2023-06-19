#####################################
# Efolio A - Simetric Encription    #
#      1902562 - Carlos Ribeiro     #
#####################################

import sys

# Function to get sum of digits 
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

# Function to encrypt file text
# Using file given in input by user
# Create another file to save the encrypt result
def encrypttext(text,s):
        
        # Variavel clean to save the result
        result = ""
        sum = getSum(s)
        diferenca = sum % 10
        
        # Function for encrypt text
        for i in range(len(text)):

                char = text[i]
                
                # Encrypt letters in plain text
                if char.isalpha() == True:
                        
                        # Encrypt uppercase characters in plain text
                        if (char.isupper()):
                                result += chr((ord(char) + s - 65) % 26 + 65)
                        else:
                                
                                # Encrypt lowercase characters in plain text
                                result += chr((ord(char) + s - 97) % 26 + 97) 
                
                elif char.isdigit() == True:

                        result += str((int(char) + diferenca) % 10)
                        
                else:
                        result += char
        return result

# Function to decrypt file text
# Using file given in input by user
# Create another file to save the decrypt result
def decrypttext(text,s):
        
        # Variavel clean to save the result
        result = ""
        sum = getSum(s)
        diferenca = sum % 10
        
        # Function for decrypt text
        for i in range(len(text)):

                char = text[i]
               
                # Decrypt letter in plain text
                if char.isalpha() == True:
                        
                        # Decrypt uppercase characters in plain text
                        if (char.isupper()):
                                result += chr((ord(char) - s- 65) % 26 + 65)
                        else:
                                
                                # Decrypt lowercase characters in plain text
                                result += chr((ord(char) - s - 97) % 26 + 97)

                elif char.isdigit() == True:

                        if int(char) - diferenca < 0:
                                result += str(10 + (int(char) - diferenca))
                        else:
                                result += str(int(char) - diferenca)
                else:
                        result += char

        return result



# Function to read file
# Read file name by user input
# Save the ile in variable conteudo
# Return conteudo
def readfile(filename):
        conteudo=""
        try:
                with open (filename) as f:
                        line = f.readline()
                        conteudo+=line
                        while line:
                                line = f.readline()
                                conteudo+=line
                        return conteudo
        except IOError as e:
                
                # Py3 f-strings
                print(f"Couldn't open or write to file ({e})")
                sys.exit()
        
# Function to create a new file
# Create file with name given in input by user
def creatfile(conteudo, filetosave):
        with open(filetosave, "w") as f:
                f.write(conteudo)

#Função Menu
def print_menu():

        print ('------------------------------------------------------------')
        print ('------ 1 -- Encrypt one file text (.txt) - Encryption ------')
        print ('------ 2 -- Decrypt one file text (.txt) - Encryption ------')
        print ('------------------------------------------------------------')
        print ('------------------------------------------------------------')
        print ('------------------------ 3 -- Exit -------------------------')
        print ('------------------------------------------------------------')
        


def Main():
        while(True):
                print_menu()
                try:
                        option = int(input('Enter your choice: '))
                except:
                        print('Wrong input. Please enter a number ...')
                        #Check what choice was entered and act accordingly
                if option == 1:

                        text = input("Enter file name with the text to encrypt: ")
                        # Run the encrypt Function
                        conteudo=readfile(text)
                
                        # User can define seed to encrypt
                        s = int (input("Enter number of seed to use: "))
                        encriptedcontent = encrypttext(conteudo,s)

                        # User can define the name of file text to get the encrypt text
                        text = input("Enter file name to get encripted message: ")
                        creatfile(encriptedcontent, text)
                        


                elif option == 2:

                        text = input("Enter file name with the text to decrypt: ")
                        # Run the decrypt Function
                        conteudo=readfile(text)

                        # User can define seed to Decrypt
                        # If not the same seed of encrypt dont get original text
                        s = int (input("Enter number of seed to use: "))
                        decriptedcontent = decrypttext(conteudo,s)

                        # User can define the name of file text to get the Decrypt text
                        text = input("Enter file name to get decripted message: ")
                        creatfile(decriptedcontent, text)

                elif option == 3:
                        print('')
                        print('Thanks')
                        exit()


                else:
                        # When nummber is not between 1 and 5, show this menssage
                        print('Invalid option. Please enter a number between 1 and 5.')
                print('')

# Main to run Function Main to run all choise User chose by input
if __name__ == '__main__':
        Main()