"""
n = int(input("введите n: "))
total_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total_sum += i
print("сумма четных чисел : ", total_sum)
"""
"""
n = int(input("введите положительное целое число :"))
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
print("количество цифр: ", count)
"""
n = int(input("введите положительное целое число:"))
temp = n
count = 0
total_sum = 0
even_count = 0
max_digit = 0
while temp > 0:
    digit = temp % 10
    count += 1
    total_sum += digit
    if digit % 2 == 0:
        even_count += 1
    if digit > max_digit:
        max_digit = digit
    temp //= 10
print("количество цифр :", count)
print("сумму цифр :", total_sum)
print("количество четных чисел :", even_count)
print("максимальная цифра :", max_digit)

