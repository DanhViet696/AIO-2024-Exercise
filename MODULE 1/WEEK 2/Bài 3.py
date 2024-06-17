def count_word(path):
    count = {}
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
    for word in words:
        word = word.lower()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

path = r'C:\Users\Admin\Desktop\viet\P1_data.txt'
result = count_word(path)
print(result)
