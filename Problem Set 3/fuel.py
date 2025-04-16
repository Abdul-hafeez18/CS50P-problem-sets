while True:
    try:
        fraction=input("Fraction: ").split("/")
        percentage=round(int(fraction[0])/int(fraction[1])*100)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except IndexError:
        pass
    else:
        if percentage>100:
            continue
        else:
            break

if percentage>=99:
    print("F")
elif percentage<=1:
    print("E")
else:
    print(int(percentage),"%", sep="")