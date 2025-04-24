import sys
import pyfiglet
input=input("input: ")
if len(sys.argv)==3:
    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        f = pyfiglet.figlet_format(input, font=sys.argv[2])
        print(f)
    else:
        print("Invalid usage" )
elif len(sys.argv) == 1:
        f = pyfiglet.figlet_format(input)
        print(f)
else:
     print("Invalid usage")

