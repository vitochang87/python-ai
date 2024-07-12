def hello():  # def 可以定義一個指令, 這個指令叫做 hello, 這個指令不需要傳入資料
    print("Hello!")


hello()


def hello2(name):  # def 可以定義一個指令, 這個指令叫做 hello2, 這個指令需要傳入一個資料
    print(f"Hello, {name}!")  # 這個指令會印出 Hello, name!


hello2("John")  # 這個指令會印出 Hello, John!
hello2("Ray")  # 這個指令會印出 Hello, Ray!


def hello3(
    name, age
):  # def 可以定義一個指令, 這個指令叫做 hello3, 這個指令需要傳入兩個資料
    print(
        f"Hello, {name}! You are {age} years old."
    )  # 這個指令會印出 Hello, name! You are age years old.


hello3("John", 18)  # 這個指令會印出 Hello, John! You are 18 years old.
hello3("Ray", 20)  # 這個指令會印出 Hello, Ray! You are 20 years old.
hello3(age=20, name="Ray")  # 這個指令會印出 Hello, Ray! You are 20 years old.


def age10(age):
    return age + 10


print(age10(18))  # 這個指令會印出 28
print(age10(20))  # 這個指令會印出 30


x = 10
print(f"x = {x}")  # 這個指令會印出 x = 10
if x > 5:
    x = 20


length = 5  # 這是全域變數
area = 3.14 * 10**2  # 這是全域變數


def calculate_square_area():  # 定義一個指令, 但還沒有執行
    global area  # 宣告area是全域變數
    area = length**2  # 計算正方形面積
    a = 10  # 這是區域變數
    print("區域變數a是", a)  # 印出區域變數a的值


calculate_square_area()  # 執行指令, 這時候全域變數area的值會被改變
print("面積是", area)
