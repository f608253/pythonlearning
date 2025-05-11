#Word game script

word = input("Enter a word: ")

word_length = len(word)
print(f"The word {word} has {word_length} characters")

#reverse the word

reversed_word = word[::-1]

print(f"The reversed word is {reversed_word}")

#create new word
first_car = word[0]
new_word = first_car * word_length
print(f"A new word: {new_word}")

#concatenate
suffix = 'ish'
word_with_suffix = word + suffix
print(f"The word with suffix is: '{suffix}': {word_with_suffix}")