"""This program runs math to calculate a matrix depending on inputed matrixes,
phone numbers, and zip codes"""

#imports
import sys
import hashlib
import numpy as np



#arrays
matrix_one = np.empty((0, 3), dtype = 'int32', order = "C")
matrix_two = np.empty((0, 3), dtype = 'int32', order = "C")

#function to enter and validate phone numbers
def phone_numbers():
    """this function is used to enter and validate phone number length and format"""
    correct = False
    while correct is False:
        number = input("Please enter your phone number in a XXX-XXX-XXXX format: \n")
        if number.count("-") == 2 and len(number) == 12:
            print("You entered: " + number)
            correct = True
        else:
            print("The number is not in correct format, please reenter ")
            correct = False

#function to validate zip codes
def zip_codes():
    """this function is used to enter and validate zip code length and format"""
    correct = False
    while correct is False:
        zip_code = input("Please enter your zip code+4 (XXXXX-XXXX): \n")
        if zip_code.count("-") == 1 and len(zip_code) == 10:
            print("You entered: " + zip_code)
            correct = True
        else:
            print("The zipcode is not in correct format, please reenter ")
            correct = False

#function for matrix addition
def matrix_addition(one, two):
    """this function adds the two matrixes together"""
    total = np.add(one, two)
    print("The matrix is: ", total)

#function for matrix subratction
def matrix_subtraction(one, two):
    """this function subtracts the two matrixes together"""
    total = np.subtract(one, two)
    print("The matrix is: ", total)

#function for element by element multiplication
def matrix_element(one, two):
    """this function multiplies the matrixes together"""
    total = np.matmul(one, two)
    print("The totals are: ", total)

#function for password encoding
def password():
    """This function is for password encoding"""
    password_input = input("Enter a password to encode: ")
    password = password_input.encode()
    print()
    print("Encoded to MD5, your password would be: ")
    print(hashlib.md5(password).hexdigest())
    print()
    print("Encoded to SHA-2 256, your password would be: ")
    print(hashlib.sha256(password).hexdigest())
    print()
    print("and in 512: ")
    print(hashlib.sha512(password).hexdigest())


def exit_program():
    """This function is to exit the program"""
    print("Thank you for using our program!")
    sys.exit(0)



#function for menu for the matrix
def matrix_menu():
    """this function is to define the menu options for the matrix"""
    print("Option a: Input your phone number and validate the format")
    print("Option b: Input your zip code and validate the format")
    print("Option c: Input values into two matrixes")
    print("Option d: Add the two matrixes together")
    print("Option e: Subtract the two matrixes")
    print("Option f: Multiply the two matrix elements together")
    print("Option z: Exit to main menu")


#function for overall menu
def main_menu():
    """This function is to define the overall menu"""
    print("Option 1: Math with phone numbers, zip codes, and matrixes")
    print("Option 2: Password encription")
    print("Option 0: Exit the program")


CHOICE = None
CHOICE_TWO = None

while CHOICE != 0:
    main_menu()

    CHOICE = input("Please select a menu choice: \n")

    if CHOICE == "1":
        while CHOICE_TWO != "z":
            matrix_menu()
            CHOICE_TWO = input("Please select a menu choice: \n")
            if CHOICE_TWO == "a":
                phone_numbers()
            elif CHOICE_TWO == "b":
                zip_codes()
            elif CHOICE_TWO == "c":
                print("For the first matrix: ")
                row_one = input("What are the row one numbers for the matrix?: ").split(' ')
                matrix_one = np.append(matrix_one, row_one)
                row_two = input("What are the row two numbers for the matrix?: ").split(' ')
                matrix_one = np.append(matrix_one, row_two)
                row_three = input("What are the row three numbers for the matrix?: ").split(' ')
                matrix_one = np.append(matrix_one, row_three)
                print("For the second matrix: ")
                row_one = input("What are the row one numbers for the matrix?: ").split(' ')
                matrix_two = np.append(matrix_two, row_one)
                row_two = input("What are the row two numbers for the matrix?: ").split(' ')
                matrix_two = np.append(matrix_two, row_two)
                row_three = input("What are the row three numbers for the matrix?: ").split(' ')
                matrix_two = np.append(matrix_two, row_three)
                matrix_one = matrix_one.astype('float')
                matrix_two = matrix_two.astype('float')
                print()
            elif CHOICE_TWO == "d":
                matrix_addition(matrix_one, matrix_two)
            elif CHOICE_TWO == "e":
                matrix_subtraction(matrix_one, matrix_two)
            elif CHOICE_TWO == "f":
                matrix_element(matrix_one, matrix_two)
            elif CHOICE_TWO == "z":
                break
            else:
                print("Please make a valid choice")
    elif CHOICE == "2":
        password()
    elif CHOICE == "0":
        exit_program()
    else:
        print("Please make a valid choice")
