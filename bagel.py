import random

GUESSES = 10

# get a three-digit number at random
rand_num = random.randint(100,999)
print(rand_num)

stringified_num = str(rand_num)

# 312
# 483

# initialize variables for correct digits and correct places at 0
# for each digit,
# check for direct equality first at same index = increment by 1 if true
# if falsy, check if that value is in the game's number at all = increment by 1 if true

# print "Bagels" if both variables are set to 0

s = input("Enter your guess for the number here:")

# validate user's guess?

guess_hints = []

j = 0
for i in range(len(s)):
    if stringified_num[i] == s[i]:
        guess_hints.append('Fermi')
    elif s[i] in stringified_num:
        guess_hints.append('Pico')

if len(guess_hints) == 0:
    print("Bagels")
else:
    feedback = ' '.join(guess_hints)
    print(feedback)

# print(s)