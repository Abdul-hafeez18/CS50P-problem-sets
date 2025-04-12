def shuroowith(greet):
    array_greet=greet.split()
    if array_greet[0]=="hello":
        x= True
    else:
        x= False
    return x
#input greeting and convert greeting into lower case
greeting=input("greeting: ").strip().lower().replace(",","")
#compare greeting as asked in project
if shuroowith(greeting):
    print("$0")
elif greeting[0]=="h":
    print("$20")
else:
    print("$100")
