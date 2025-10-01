# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다.
# 항상 "ICN" 공항에서 출발합니다.

# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때,
# 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

# 입출력 예
# tickets	            return
# [["ICN", "JFK"],
# ["HND", "IAD"],
# ["JFK", "HND"]]	    ["ICN", "JFK", "HND", "IAD"]

# [["ICN", "SFO"],
# ["ICN", "ATL"],
# ["SFO", "ATL"],
# ["ATL", "ICN"],
# ["ATL","SFO"]]	    ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# 경로니까 DFS?


# 1
def solution(tickets):
    tickets.sort()
    n = len(tickets)

    used = [False] * n
    route = ["ICN"]

    def dfs(cur, depth):
        if depth == n:
            return True

        for i, (a, b) in enumerate(tickets):
            if not used[i] and a == cur:
                used[i] = True
                route.append(b)
                if dfs(b, depth + 1):
                    return True
                route.pop()
                used[i] = False
        return False

    dfs("ICN", 0)
    return route


# 2
from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for a in graph:
        graph[a].sort(reverse=True)  # 뒤에서 pop()하려고 역정렬

    route = []
    stack = ["ICN"]

    while stack:
        cur = stack[-1]
        if graph[cur]:
            stack.append(graph[cur].pop())  # 가장 작은 목적지부터 소비
        else:
            route.append(stack.pop())  # 막다른 곳이면 경로 확정(후위)
    return route[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
