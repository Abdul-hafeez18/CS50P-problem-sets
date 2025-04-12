#input the word
exp=input("input: ").split(" ")
match exp[1]:
    case "+":x= float(exp[0])+float(exp[2])
    case"-": x=float(exp[0])-float(exp[2])
    case"*": x=float(exp[0])*float(exp[2])
    case"/": x=float(exp[0])/float(exp[2])
    case _: print("not applicaple")
print(x)