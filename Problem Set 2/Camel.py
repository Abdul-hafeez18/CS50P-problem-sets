def capital_finder(word):
   # new_letter=None
    print("SnakeCase :", end="")
    for letter in range(len(word)):
        if word[letter].isupper():
            print("_", end="")
        new_letter=word[letter].lower()
        print(new_letter, end="")
        
def main():
    CamelCase=input("CamelCase: ")
    capital_finder(CamelCase)

main()