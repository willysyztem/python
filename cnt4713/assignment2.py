#William Valido
#3354913
#Professor: Alex Afanasyev
#Class: CNT4713 RVC 1208

import socket

class Assignment2:
    def __init__ (self, age):
        self.age = age

    def sayWelcome(self, name):
        print (f"Welcome to the assignment, {name}!  Haven't seen you for {self.age} years!")

    def doubleList(self, input):
        firstHalf = []
        secondHalf = []

        for index, item in enumerate(input):
            newString = item + item
            firstHalf.append(newString)
            
        odd = []
        even = []
        for index, item in enumerate(input):
            if(index % 2 == 0):
                even.append(input[index])
            else:
                odd.append(input[index])
        secondHalf = (even + odd)
        return (firstHalf + secondHalf)

    def modifyString(self, name):
        modifiedString = list(name)
        for index, item in enumerate(name):
            pos = index + 1
            if(pos % 3 == 0):
                modifiedString[index] = item.upper()
            if(pos % 4 == 0):
                if(pos % 3 != 0):
                    modifiedString[index] = item.lower()
            if(pos % 5 == 0):
                if((pos % 3 != 0) and (pos % 4 != 0)):
                    modifiedString[index] = ' '
        return("".join(modifiedString))

    @staticmethod
    def isGoodPassword(password):
        #check for total lower case
        hasLowerCase = False
        lowerCaseCount = 0
        minLowerAllowed = 2
        #check for total upper case
        hasUpperCase = False
        upperCaseCount = 0
        minUpperAllowed = 3
        #check for total special characters
        hasSpecialChars = False
        specialCharsCount = 0
        minSpecialAllowed = 2
        #check for digits
        hasDigit = False

        if(len(password) >= 9):
            for item in password:
                if item.islower():
                    lowerCaseCount += 1
                if item.isupper():
                    upperCaseCount += 1
                if (item in '.,#('):
                    specialCharsCount += 1
                if item.isnumeric():
                    hasDigit = True

            if(lowerCaseCount >= minLowerAllowed):
                hasLowerCase = True
            if(upperCaseCount >= minUpperAllowed):
                hasUpperCase =  True
            if(specialCharsCount >= minSpecialAllowed):
                hasSpecialChars = True

        if((hasLowerCase or hasUpperCase) and (hasSpecialChars or hasDigit)):
            return True
        else:
            return False

    def connectTcp(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = (host, port)

        try:
            sock.connect(serverAddress)
            sock.close()
            return True
        except socket.error:
            return False