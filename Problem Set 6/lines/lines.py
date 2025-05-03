import sys

count = 0

if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    print(f"Number of lines in {sys.argv[1]}:")

    try:
        with open(sys.argv[1], "r") as file:
            for line in file:
                if line.strip() and not line.lstrip().startswith("#"):
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)

elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
