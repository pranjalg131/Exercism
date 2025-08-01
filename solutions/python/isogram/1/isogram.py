from collections import Counter


def is_isogram(string):
    counter = Counter(string)
    allowed = [" ", "-"]

    for letter in counter.keys():
        actual_count = counter[letter] + counter[letter.swapcase()]
        if actual_count > 1 and letter not in allowed:
            return False

    return True
