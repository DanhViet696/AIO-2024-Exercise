def count_letters(word):
    # Khởi tạo một dictionary để lưu kết quả
    letter_count = {}

    # Đưa tất cả các ký tự trong từ về chữ thường để đếm đúng
    word = word.lower()

    # Đếm số lần xuất hiện của từng ký tự trong từ
    for char in word:
        if char.isalpha():  # Chỉ xét các ký tự là chữ cái
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

# Ví dụ sử dụng
word = "Hello, World!"
result = count_letters(word)
print(result)

