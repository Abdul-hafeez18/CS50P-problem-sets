word=input("input: ")
new_word=[]
vowels=["a","e","i","o","u","A","E","I","O","U"]
for letter in word:
    if letter not in vowels:
        new_word.append(letter)
print("".join(new_word))
