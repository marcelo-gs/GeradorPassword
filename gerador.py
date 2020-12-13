
__author__ = "Marcelo Gomes"
__email__  = "marcelo.gs@terra.com.br"

import random

#A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
digit1=chr(random.randint(48,57)) #Generate a random digit letter (based on ASCII code)
digit2=chr(random.randint(48,57)) #Generate a random digit letter (based on ASCII code)
specialChar1=chr(random.randint(33,47)) #Generate a random specialChar letter (based on ASCII code)
specialChar2=chr(random.randint(58,64)) #Generate a random specialChar letter (based on ASCII code)

#Generate String with all letters genereted
password = uppercaseLetter1 
password += uppercaseLetter2 
password += lowercaseLetter1 
password += lowercaseLetter2 
password += digit1 
password += digit2 
password += specialChar1
password += specialChar2

#shuffle string to dificult things
password = shuffle(password)

#Ouput
print(password)