#make main function and input time
#def main():
    #real_time=input("What time is it: ")
    #real_time=convert(real_time)
#make convert function which convert string to float
#def convert(time):

# time=input("input time")
# time=time.strip().replace(":"," ").split()
# just_time=str(float(time[1])/60)
# just_time=just_time.replace(".","").split()
# just_time=just_time.remove(just_time[0])
# new_time=time.insert(0,just_time)
# new_time="".join(new_time)
# new_time=float(new_time.replace(" ","."))
# print("time is: ", new_time)

def main():
    time = input("What time is it ? ")
    updated_time = convert(time)
    if 7<=updated_time<=8:
        print("breakfast time")
    elif 12<=updated_time<=13:
        print("lunch time")
    elif 18<=updated_time<=19:
        print("dinner time")
    else:
        print("")
    



def convert(time):
    time = time.split(":")
    time[1] = int(time[1])/60
    time = int(time[0]) + (time[1])
    return time


if __name__ == "__main__":
    main()