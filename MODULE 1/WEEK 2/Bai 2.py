def count_letters(word):
    text_count = {}
    word = word.lower()
    for char in word:
        if char.isalpha():
            if char in text_count:
                text_count[char] += 1
            else:
                text_count[char] = 1

    return text_count
word = "Hello"
result = count_letters(word)
print(result)