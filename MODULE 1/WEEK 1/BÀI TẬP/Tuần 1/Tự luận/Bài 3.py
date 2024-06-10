import random
import math


def calculate_loss(num_samples, loss_name):
    # Kiểm tra tính hợp lệ của num_samples
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return

    num_samples = int(num_samples)

    # Tạo các giá trị predict và target ngẫu nhiên
    predicts = [random.uniform(0, 10) for _ in range(num_samples)]
    targets = [random.uniform(0, 10) for _ in range(num_samples)]

    # Tính toán loss dựa trên loss_name
    if loss_name == "MAE":
        loss = sum(abs(targets[i] - predicts[i]) for i in range(num_samples)) / num_samples
    elif loss_name == "MSE":
        loss = sum((targets[i] - predicts[i]) ** 2 for i in range(num_samples)) / num_samples
    elif loss_name == "RMSE":
        mse = sum((targets[i] - predicts[i]) ** 2 for i in range(num_samples)) / num_samples
        loss = math.sqrt(mse)
    else:
        print("Invalid loss name")
        return

    # Print ra kết quả
    print(f"loss name: {loss_name}")
    for i in range(num_samples):
        print(f"sample-{i}: predict = {predicts[i]:.4f}, target = {targets[i]:.4f}")
    print(f"loss: {loss:.4f}")


# Input từ người dùng
num_samples = input("Enter number of samples: ")
loss_name = input("Enter loss name (MAE, MSE, RMSE): ")

# Gọi function để tính toán và in ra kết quả
calculate_loss(num_samples, loss_name)
