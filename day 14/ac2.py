#world frequency counter
def word_count(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_count("The sun rises in the east and the sun sets in the west"))

