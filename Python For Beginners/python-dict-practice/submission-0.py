from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    if len(word) < 0:
        return {}
    result = {}
    for letter in word:
        if letter in result:
            result[letter] = result[letter] + 1
        else:
            result[letter] = 1

    return result

        




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
