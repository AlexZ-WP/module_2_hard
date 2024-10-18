number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum_number = []


for i in list_:
    for j in list_2:
        if i == j:
            continue
        else:
            sum_number.append(i + j)
            continue
for i in number:
    for j in sum_number:
        if i == j and i < j:
            continue
        if i % j == 0:
            break
print('result: ', j)