q = 0
t = 0
c = 0
r = 0
print("you need to tell me a password with 6-16 characters, one has to be upper case, one lower case, one digit, and one of the following #$%")
def passw():
    x = input("tell me a password. ")
    if len(x) > 16 or len(x) < 6:
        print("that password is too long try or too short again ")
        ask = input("if you want to start again then type the words, try again. If not type something else.")
        if ask == "try again":
            passw()
    else:
        for a in range(len(x)):
            b = x[a]
            if b >= "A" and b <= "Z":
                q = 1
            if b >= "a" and b <= "z":
                t = 1
            if b >= "0" and b <= "9":
                c = 1
            if b == "$" or b == "@" or b == "#":
                r = 1
        if q == 1 and t == 1 and c == 1 and r == 1:
            print("your password works!")
        else:
            print("this password doesn't work. Try again.")
            ask = input("if you want to start again then type the words, try again. If not type something else.")
            if ask == "try again":
                passw()
        
                
passw()
            
    
            
