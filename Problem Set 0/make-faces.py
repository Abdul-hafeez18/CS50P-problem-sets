#replace the word by making function convert
def convert(word):
    new_word=word.replace(":)",":slightly_smiling_face:").replace(":(",":slightly_frowning_face:")
    return new_word
#make main function and call convert
def main():
    phrase=input("input the word")
    new_phrase=convert(phrase)
    print(new_phrase)

main()
