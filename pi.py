text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
###
words = text.split()
my_list=list(map(len, words))
pi_string = ''
for num in my_list:
    pi_string += str(num)
print(pi_string)
