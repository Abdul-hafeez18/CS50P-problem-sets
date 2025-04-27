def main():
    akhar=input("input: ")
    print(shorten(akhar))
    


def shorten(word):
        new_word=[]
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        for letter in word:
            if letter not in vowels:
                new_word.append(letter)
        x="".join(new_word)
        return x



if __name__ == "__main__":
    main()
