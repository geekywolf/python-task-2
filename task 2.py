import string
import random

def userInput():
    """
    This function acts as a template to collect and store user details
    """
    userInput.firstName = str(input("Enter your First name:   ")).capitalize()
    userInput.lastName = str(input("Enter your Last name:   ")).capitalize()
    userInput.Email = input("Enter your Email:   ")
    userInput.extra = ''.join(random.choice(string.ascii_letters) for x in range(5))
    userInput.password = userInput.firstName[:2] + userInput.lastName[-2:] + userInput.extra

def newUser():
    """
    This functions takes the input and stores it into a python dictionary to be loaded into a static dictionary
    """
    userInput

    dictionary = { 
        'Name' : userInput.firstName +" "+ userInput.lastName,
        'Email' : userInput.Email,
        'Password' : userInput.password
        }
    
    return dictionary


def userDetails():
    """
    This function acts as a template for displaying user details
    """
    userInput
    return print(f"""\n\n
    First Name\t:\t {userInput.firstName} \n
    Last Name\t:\t {userInput.lastName} \n
    Email\t:\t {userInput.Email} \n 
    Password\t:\t {userInput.password}""")
    
userInput()

"""This is a dynamic dictionry storage that uses the email as primary key"""
Storage ={

    userInput.Email: newUser()
}

user_choice = str.lower(input(f"Your password is:    {userInput.password} \n Are you satisfied with your password? Please input yes or no:  "))

if user_choice == 'yes':
    userDetails()
    print(Storage)
else:
    control  = True
    
    while control:
        
        password = input("\n\n***NOTE THAT YOUR PASSWORD MUST BE 7 LETTERS OR MORE*** \nEnter your password:   ")
        if len(password) < 7:
            control = False
            print("Enter a password of more than 7 characters")
            x = str.lower(input('Type yes when youre ready to retype password:  '))
            if x == "yes":
                control = True
            else:
                print(userDetails())
        else:
            userInput.password = password
            print(userDetails())
            print(Storage)
            control = False
