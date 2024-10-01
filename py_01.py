def middleChar(word: str) -> str:
    if len(word) % 2 == 1:
        return word[len(word) // 2]
    else:
        return word[len(word) // 2 - 1: len(word) // 2 + 1]


print(middleChar("test"))
print(middleChar("testing"))