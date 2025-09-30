# dynamic programming
# 어떤 문제를 이전에 풀었던 더 작은 문제를 바탕으로 풀겠다.


# ex)
# 피보나치
def fibo(n):
    print(n)
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


# print('정답 : ', fibo(8))

# 재귀의 문제점 : 연산의 중복. f(n-3)같은걸 여러번 실행해야 한다.

# dp 핵심 : 이전 단계를 저장해 둔다.


# bottom up
# n = 1, 2, 3, 4 ... 순서대로 값을 만들어갑니다.
# tabulation
def fibo(n):
    lst = [0] * (n + 1)
    # base case
    lst[1] = 1
    lst[2] = 1
    for i in range(3, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    return lst[n]


# print('정답 : ', fibo(8))
#
# top down
# memoization
def fibo(n):

    lst = [0] * (n + 1)
    lst[1] = 1
    lst[2] = 1

    def fibo_helper(n):
        # print(n)
        if lst[n] == 0:
            lst[n] = fibo_helper(n - 1) + fibo_helper(n - 2)
        return lst[n]

    fibo_helper(n)

    return lst[n]


print("정답 : ", fibo(8))
