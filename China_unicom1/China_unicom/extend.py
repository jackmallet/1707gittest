l1 = [1, 2, 3, 4, 5, ]
l1.append([6, 7, 8, 9, ])
# l1.append(*[6, 7, 8, 9, ]) #会报错
print(l1)
l1.extend([6, 7, 8, 9])
print(l1)