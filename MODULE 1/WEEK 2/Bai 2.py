def count_letters(word):
    text_count = {}  # Đổi tên biến count thành text_count hoặc tên khác phù hợp
    word = word.lower()
    for char in word:  # Sử dụng char để duyệt từng ký tự trong từ
        if char.isalpha():  # Kiểm tra xem char có phải là chữ cái không
            if char in text_count:
                text_count[char] += 1
            else:
                text_count[char] = 1

    return text_count


# Ví dụ sử dụng
word = "data"
result = count_letters(word)
print(result)
