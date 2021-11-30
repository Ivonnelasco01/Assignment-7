#input sentence
#count words
#count vowels
#count consonants

sentence = input("Enter a Sentence here: ")
space_count = 0

for character in sentence:
    if character == " ":
        space_count = space_count + 1
number_of_words = space_count + 1

print("You entered: ",sentence)
print("number of words: ", number_of_words)