numbers = [2, 4, 100, 6, 9, 0, 3]

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            greaterNum = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = greaterNum
print(numbers)


# for i in range(2, len(numbers), 2):
#     # print(numbers[i - 2], numbers[i])

#     a = numbers[i]
#     numbers[i] = numbers[i-2]
#     numbers[i-2] = a

# # for i in range(2, len(numbers), 2):
# print(numbers)
