l = [1, 2, 3]
l.append(4)
print(l)

l = ["a", "b", "c", "a"]
l.remove("a")
print(l)

l = [9, 1, -4, 3, 7, 11, 3]
print(l.count(3))

L = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]  # 這是一個包含十個元素的list
c = L.count(3)  # 把八加到L的最後面
for i in range(c):  # 將八加到L的最後面
    L.remove(3)

print(L)  # 印出L


L.pop(0)  # 刪除L中的第o個元素
print(L)  # 印出L
# pop 與 remove 的差別：pop 是用index, remove適用元素來刪除

L.sort()  # 將L中的元素由大到小排序
print(L)  # 印出L
L.sort(reverse=True)  # 將L中的元素由小到大排序
print(L)  # 印出L


print(l.index(5))  # 取出L中的5的index
