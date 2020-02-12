"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
            


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    
    rand = random.randint(1,9)
    while(1):
        inp = input("enter a guess (1-9 inclusive")
        if inp == "exit":
            break
        elif int(inp) == rand:
            print("you win (exactly right)")
            break
        elif int(inp) < rand:
            print("guess too low")
        else:
            print("guess too high")


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
   
    for i in range(0,int(len(string)/2)):
        if string[i] != string[len(string)-1-i]:
            print("False")
            return False
    else:
        print("True")
        return True
        
def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    f = open(filename, "w")
   
    encodedUser = base64.b64encode(username.encode("utf-8"))
    encodedUser1 = str(encodedUser, "utf-8")
    encodedPass = base64.b64encode(password.encode("utf-8"))
    encodedPass1 = str(encodedPass, "utf-8")
    f.write(encodedUser1 + "\n" + encodedPass1)
    

part4a("beeeep.txt","username","password")

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    with open(filename, "r") as f1:
        data = f1.readlines()
    
    user = data[0]
    pword = data[1]
    
    decodedUser = base64.b64decode(user)
    decodedUser1 = str(decodedUser, "utf-8")
    decodedPass = base64.b64decode(pword)
    decodedPass1 = str(decodedPass, "utf-8")
    
    print(decodedUser1 + " " + decodedPass1)
    
    if password != None:
        encodedPass = base64.b64encode(password.encode("utf-8"))
        encodedPass1 = str(encodedPass, "utf-8")
        data[1] = encodedPass1 + '\n'
        with open(filename, "w") as f1:
            f1.writelines(data)


        
if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")


