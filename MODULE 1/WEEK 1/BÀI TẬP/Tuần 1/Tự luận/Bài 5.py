import math


def nth_root_error(y, y_hat, n, p):
    if n == 0:
        print("n cannot be zero")
        return None

    nth_root_y = y ** (1 / n)
    nth_root_y_hat = y_hat ** (1 / n)
    error = abs(nth_root_y - nth_root_y_hat) ** p
    return error


# Input values for testing
y = 3
y_hat = 34
n = 5
p = 1

# Calculate and print the error
error = nth_root_error(y, y_hat, n, p)
print(f'The nth root error for y={y}, y_hat={y_hat}, n={n}, p={p} is: {error}')
