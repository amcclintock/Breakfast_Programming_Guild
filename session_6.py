#Pig Latin translator

#English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding ‘ay’. “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.


#Flip the word into pig latin
def translate_word(word):
    vowels = 'aeiou'
    first_letter, *remaining_letters = word.lower()

    if first_letter in vowels:
        return word + 'yay'
    else:
        return ''.join(remaining_letters) + first_letter + 'ay'


#Break apart the sentence into words, then combine new words back together again
def translate_sentence(sentence):
    translated_sentence = ""
    for word in sentence.split(" "):
        translated_sentence += translate_word(word) + " "

    return translated_sentence.strip()



#Call the functions, and return the value
print(translate_sentence('The quick brown fox'))


#Challenge

# Take sentence(s) from user, ensure no punctuation.  Use a loop(s) to take in many sentences