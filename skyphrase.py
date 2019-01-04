        
def countValidPasswords(path):
    '''
    Function that validates passwords in specified file and counts its number
    '''
    with open(path) as file:
        text = file.readlines()
    
    validPasswdsCounter = 0
    for passwd in text:
        passwdList = passwd.split()
        if len(passwdList) == len(set(passwdList)):
            validPasswdsCounter += 1
    
    return validPasswdsCounter
        
        
n = countValidPasswords('skyphrase_input.txt')
print("Number of valid passwords in file: " , n, "\n")
input('Press any key to exit')