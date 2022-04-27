counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        letter = word[0]

        if letter in counts:  # if seen letter before
            counts[letter] += 1
            # counts[letter] = counts[letter] + 1
        else:
            counts[letter] = 1

for letter, count in counts.items():
    print(letter, count)

