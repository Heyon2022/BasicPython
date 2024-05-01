text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
###
#問2
import string

text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
words = text_without_punctuation.split()
word_lengths = [len(word) for word in words]
pi_string = ''.join(map(str, word_lengths))
print(pi_string)




