import random
def PasswordGenerator(pwl):
    alphabet = "abcdefghijklmnopqrstuvwxyz#@1234567890"
    password = "" 
    for j in range(pwl):
        index = random.randint(0, len(alphabet)-1)
        password = password + alphabet[index]  
    password = replaceWithNumber(password)
    password = replaceWithUppercaseLetter(password)   
    return password
def replaceWithNumber(pword):
    for i in range(random.randint(1,2)):
        index = random.randint(0, len(pword)//2)
        pword = pword[0:index] + str(random.randint(0,9)) + pword[index+1:]
    return pword
def replaceWithUppercaseLetter(pword):
    for i in range(random.randint(1,2)):
        index = random.randint(0, len(pword)//2)
        pword = pword[0:index] + pword[index].upper() + pword[index+1:]
    return pword

length = int(input("Enter the length of Password: "))
print("Generated Password is: ",PasswordGenerator(length))