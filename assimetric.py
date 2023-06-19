#####################################
# Efolio A - Assimetric Encription  #
#      1902562 - Carlos Ribeiro     #
#####################################


import math
import sys

# ------------ Pedido do P e do Q para o algoritmo RSA ------------ #

# Funcao auxiliar para descobrir se o numero dado e primo (P, Q)
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# Funcao de setup para o algoritmo RSA para descobrir as chaves
def setup():

    print ('------------------------------------------------------------')
    print("The RSA algorithm requires initial values according to the equation:")
    print("X * Y = (P - 1) * (Q - 1) + 1, where...")
    print("\tX is the generated public key;")
    print("\tY is the generated private key;")
    print("\tP is the first given prime number;")
    print("\tQ is the second given prime number;")
    print ('------------------------------------------------------------')

    # Apenas numeros primos para P
    #Quanto maior o numero melhor para o modulo PQ ser maior e poder encriptar uma parte maior 

    p = int(input('Enter the first prime number (p): '))
    if p <= 0:
        print("p not given or too small, changing it to default (1009)")
        p = 1009

    # Apenas numeros primos para Q
    #Quanto maior o numero melhor para o modulo PQ ser maior e poder encriptar uma parte maior

    q = int(input('Enter the second prime number (q): '))
    if q <= 0:
        print("p not given or too small, changing it to default (2741)")
        q = 2741


    x = int(input('Enter a initial value for x: '))
    if x <= 0:
        print("x not given or too small, changing it to default (1)")
        x = 1

    print ('------------------------------------------------------------')

    # Se P ou Q nao for primos, dá erro

    if not is_prime(p) or not is_prime(q):
        raise ValueError('P or Q were not prime')

    pq = p * q
    eq = (p - 1) * (q - 1) + 1

    y = 1
    xy = x*y

    while xy != eq:
        x += 1
        y = eq // x
        xy = x*y
    
    print("Your public key (X) is: " + str(x))
    print("Your private key (Y) is: " + str(y))
    print("Your module (p*q) is: " + str(pq))

    return {"x": x, "y": y, "pq": pq}

def rsa_encrypt_text(public_key: list[int, int], plaintext: str) -> str:

    # encriptar um ficheiro de texto usando a chave publica, transformando tudo em números

    x, pq = public_key

    # jajah-se
    # '927-8267-927-8267-735-60-09;
    # jajah-se
    encrypted = ''
    for letter in plaintext:
        encrypted += str(((ord(letter) ** x) % pq))
        encrypted += '-'

    return encrypted[:-1]


def rsa_decrypt_text(private_key: list[int, int], ciphertext: str) -> str:

    # desencriptar um ficheiro de texto usando a chave privada
    #transforma os numeros separados por '-' em letras

    y, pq = private_key

    # jajah-se
    # '927-8267-927-8267-735-60-09';
    # jajah-se
    decrypted = ''
    listadcr = ciphertext.split('-')
    # ['927', '8256', ...]
    for number in listadcr:
        decrypted = decrypted + chr((int(number) ** y) % pq)

    return decrypted

# Função ler ficheiro

def readfile(filename):
        conteudo=""
        try:
                with open (filename) as f:
                        line = f.readline()
                        conteudo+=line
                        while line:
                                line = f.readline()
                                conteudo+=line
                        f.close()
                        return conteudo
        except IOError as e:
                
                # Py3 f-strings
                print(f"Couldn't open or write to file ({e})")
                sys.exit()

# Função criar novo ficheiro
def creatfile(conteudo, filetosave):
        with open(filetosave, "w",  encoding="utf-8") as f:
                f.write(conteudo)
        f.close()

#Função Menu
def print_menu():
        print ('------------------------------------------------------------')
        print ('------ 1 -- Encrypt one file text (.txt) - Encryption ------')
        print ('------ 2 -- Decrypt one file text (.txt) - Decryption ------')
        print ('------------------------------------------------------------')
        print ('------ 3 ------- Encrypt one number - Encryption -----------')
        print ('------ 4 ------- Decrypt one number - Decryption -----------')
        print ('------------------------------------------------------------')
        print ('------ 5 ----------------- Exit Program --------------------')
        print ('------------------------------------------------------------')


def main():

    dictcrp = {}
    dictcrp = setup()

    while (True):
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

            print("Encripting file with " + str(dictcrp["x"]) + " as the public key...")
            print("\t... and " + str(dictcrp["pq"]) + " as P*Q")

            encriptedcontent = rsa_encrypt_text([dictcrp["x"], dictcrp["pq"]], conteudo)

            # User can define the name of file text to get the encrypt text
            text = input("Enter file name to get encripted message: ")
            creatfile(encriptedcontent, text)

        elif option == 2:

            text = input("Enter file name with the text to decrypt: ")
            # Run the decrypt Function
            conteudo = readfile(text)

            print("Decripting file with " + str(dictcrp["y"]) + " as the private key...")
            print("\t... and " + str(dictcrp["pq"]) + " as P*Q")

            decriptedcontent = rsa_decrypt_text([dictcrp["y"], dictcrp["pq"]], conteudo)

            # User can define the name of file text to get the Decrypt text
            text = input("Enter file name to get decripted message: ")
            creatfile(decriptedcontent, text)

        elif option == 3:
            
            # Numero a codificar

            m = int(input("Enter your number to encript: "))

            # Se M maior que o PQ dá erro, não é possivel
            # Quando ultrapassa o módulo

            if m >= dictcrp["pq"]:
                raise ValueError('m its bigger that module')

            print("Encripting file with " + str(dictcrp["x"]) + " as the public key...")
            print("\t... and " + str(dictcrp["pq"]) + " as P*Q")

            res = m ** dictcrp["x"]
            encrypted_message = res % dictcrp["pq"]

            print('Your encrypted message is: ' + str(encrypted_message))  

        elif option == 4:
            
            # Numero a codificar

            m = int(input("Enter your number: "))

            # Se M maior que o PQ dá erro, não é possivel
            # Quando ultrapassa o módulo

            if m >= dictcrp["pq"]:
                raise ValueError('m its bigger that module')

            print("Decripting file with " + str(dictcrp["y"]) + " as the private key...")
            print("\t... and " + str(dictcrp["pq"]) + " as P*Q")

            res = m ** dictcrp["y"]
            encrypted_message = res % dictcrp["pq"]

            print('Your decrypted message is: ' + str(encrypted_message))

        elif option == 5:
            sys.exit()

        else:
            # When number is not between 1 and 5, show this menssage
            print('Invalid option. Please enter a number between 1 and 4.')
            print('')
                    
# Main to run Function Main to run all choise User chose by input
if __name__ == '__main__':
        main()