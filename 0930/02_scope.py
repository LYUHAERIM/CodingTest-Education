# 변수를 접근할 때, 어느 수준까지 접근이 가능할까?

x = 100


def func():
    print("1번째", x)


func()


########################

x = 100


def func():
    x = "abc"
    print("2번째", x)


func()

########################

x = 100


def func():
    x = "abc"


func()
print("3번째", x)

########################
# global : 함수 내부에서 사용하는 변수 -> global 환경에서 사용하는 변수와 같게 취급.
# 즉, 함수 내부에서 global변수를 변경할 수 있다.
x = 100


def func():
    global x
    x = "abc"


func()
print("4번째", x)

########################
# 개발할때는 하면 안되는 행동.
# 단, 알고리즘 풀때는 매우 유용.
lst = [1, 2, 3]


def func():
    lst.append(10)


func()
print("5번째", lst)
