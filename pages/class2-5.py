print([])  # 這是一個空的list
print["蘋果"]  # 這是一個有兩個元素的list
print["a", "b"]  # 這是一個有六個元素的list
print[1, 2, 3]  # 這是一個有四個元素的list

L = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(L[0])  # 取出L中的第一個元素, 元素編號(index)是從0開始
print(L[1])  # 取出L中的第二個元素
print(L[2])  # 取出L中的第三個元素

for index in range(len(L)):
    print(L[index])  # 取出L中的第index個元素

for index in L:
    print(index)  # 取出L中的第index個元素

L[0] = "moo"  # 將L中的第一個元素改成"moo"
