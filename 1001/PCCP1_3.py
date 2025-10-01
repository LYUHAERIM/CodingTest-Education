def solution(queries):
    # queries에 담긴 순서대로 n세대의 p 번째 개체의 형질
    answer = []
    for n, p in queries:
        # n, p를 활용해서
        gene = get_gene(n, p)
        answer.append(gene)
    return answer


# 세대와 순서를 받아서 형질을 return하는 함수.
def get_gene(n, p):
    if n == 1:
        return "Rr"
    # n : 세대
    # p : 순서

    # 만약 부모의 형질을 알면 나의 형질을 p를 바탕으로 알 수 있음.
    # 부모가 RR -> RR
    # 부모가 rr -> rr
    # 부모가 Rr -> 순서에 따라 정해져.

    # parent = get_gene(n', p')
    # n', p'이 어떻게 정해지느냐?
    # 부모는 자식의 순서 를 4로 나눈 몫. 단, 1부터 시작하기 때문에 맞춰주기 위해 1을 빼준다.
    parent = get_gene(n - 1, (p - 1) // 4 + 1)

    if parent == "RR":
        return "RR"

    if parent == "rr":
        return "rr"

    # if parent == 'Rr':
    # 순서에 따라 정해져.
    remainder = p % 4
    if remainder == 1:
        return "RR"
    if remainder == 0:
        return "rr"
    # if remainder == 2 or remainder == 3:
    return "Rr"
