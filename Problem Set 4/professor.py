from random import randint

def main():
    global_count=0
    level_count=0
    while global_count<=10:
        level=0
        local_count=0
        if level_count==0:
            get_level(level)
            level_count+=1
        num1=generate_integer()
        num2=generate_integer()
        while local_count<3:
            print(num1,"+", num2," = " ,end="")
            answer=int(input(""))
            if answer==(num1+num2):
                break
            else:
                print("EEE")
                local_count+=1
            if local_count>2:
                    print(num1+num2)
        global_count+=1
                





def get_level(demo_level):
    while True:
        demo_level=int(input("Level: "))
        if demo_level==1 or demo_level==2 or demo_level==3:
            break
    


def generate_integer():
    x=randint(1,9)
    return x


if __name__ == "__main__":
    main()
