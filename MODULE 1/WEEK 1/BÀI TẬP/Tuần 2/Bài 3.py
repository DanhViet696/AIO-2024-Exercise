def count_word(path):
    count = {}  # Khởi tạo một từ điển để lưu trữ số lần xuất hiện của từng từ
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()  # Đọc toàn bộ nội dung của file vào biến text
        words = text.split()  # Tách các từ trong nội dung thành một danh sách các từ

    # Đếm số lần xuất hiện của mỗi từ trong danh sách các từ
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

