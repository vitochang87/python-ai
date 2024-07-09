for i in range(10):  # i是迴圈的變數, range(10)適從0到9的數字
    print(i)  # i  每次只從range(10)中取出一個數字,從0到9

for i in range(2, 100):  # range(2,100)適從2到99的數字
    print(i)  # i  每次只從range(2,100)中取出一個數字,從2到99

for i in range(2, 100, 2):  # range(100,2,-1)適從100到2的數字
    print(i)  # i  每次只從range(2,100,2)中取出一個數字,從2到99的偶數

    for j in range(100, 3, -2):  # range(100,3,-2)適從100到4的數字,每次取出的數字是偶數
        print(j)  # j  每次只從range(100,3,-2)中取出一個數字,從100到4的偶數
