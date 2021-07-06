#Pig Latin translator

#English is translated to Pig Latin by taking the first letter of every word, moving it to the end of the word and adding ‘ay’. “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.


#Flip the word into pig latin
def translate_word(word):
    vowels = 'aeiou'
    
    # go over list slicing
    # We can access characters in a string as a list.
    # [0] => get 0th index. (1st character in the string)
    # lists can be sliced easily in python
    # [0:2] => get the first 2 character (0 and 1 index - index 2 is NOT included)
    # [1:] => get the 1st index and everything after
    lower_case_word = word.lower()
    first_letter = lower_case_word.lower()[0]
    remaining_letters = lower_case_word.lower()[1:]

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
