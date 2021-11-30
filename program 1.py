#input sentence
#count words
#count vowels
#count consonants

sentence = input("Enter a Sentence here: ")
space_count = 0
vowels_count = 0

list1 = ["a","e","i","o","u","A","E","I","O","U"]

for character in sentence:
    if character == " ":
        space_count = space_count + 1
number_of_words = space_count + 1

for character in sentence:
    if character in list1:
        vowels_count = vowels_count + 1

print("You entered:",sentence)
print("Number of words:", number_of_words)
print("Number of vowels:", vowels_count)