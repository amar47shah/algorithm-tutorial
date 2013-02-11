from mod2 import Mod2

while True:

    print
    x = Mod2(raw_input("Enter 0 or 1. "))
    y = Mod2(raw_input("Enter 0 or 1. "))
    op = raw_input(" + or * ? ")

    if op == '+':
        print x, "+", y, "=", x + y
    elif op == '*':
        print x, "*", y, "=", x * y
       
    if raw_input("Quit (y/n)? ") in ('y', 'Y'):
        break
