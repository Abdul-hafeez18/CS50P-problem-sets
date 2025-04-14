def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    if string[0] == "O":
        return False
    if  len(string)<1 and len(string)>7:
        return False
    if len(string)>2:
        if not string[0].isalpha() or not string[1].isalpha():
            return False
    else:
        if not string[0].isalpha():
            return False
    if not all(ch.isalnum() for ch in string):
        return False

    x = False
    for ch in string:
        if ch.isdigit():
            x = True
        if ch.isalpha() and x:
            return False

    for ch in string:
        if ch.isdigit():
            return ch != "0"
    if string[0] != "H":
        return True


if __name__ == "__main__":
    main()
