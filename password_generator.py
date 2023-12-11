import random
from string import ascii_letters, digits, punctuation

pass_num = int(input("Number of Passwords To Generate: "))
num = int(input("Password Length: "))
print("""Choose 1 or 2
      1. AlphaNumeric Password
      2. Password with special characters""")
choice = int(input(">> "))


def main():
    if choice == 1 or choice == 2:
        name = input("File name to save passwords: ")
        for _ in range(pass_num):
            #print(generate_password(num, choice))
            with open(name, "a") as f:
                f.writelines(generate_password(num, choice)+"\n")
    else:
        print("Please choose 1 or 2 only")
        

def generate_password(n, c):
    password = ""
    for _ in range(n):
        if c == 1:
            password += random.choice(ascii_letters+digits)
        elif c == 2:
            password += random.choice(ascii_letters+digits+punctuation)       
    return password


if __name__ == "__main__":
    main()