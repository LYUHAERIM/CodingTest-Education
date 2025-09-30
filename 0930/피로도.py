# 문제 설명
# XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며,
# 일정 피로도를 사용해서 던전을 탐험할 수 있습니다.
# 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와
# 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다.
# "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며,
# "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다.
# 예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는
# 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

# 이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데,
# 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다.
# 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴
# 2차원 배열 dungeons 가 매개변수로 주어질 때,
# 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# k	    dungeons	                result
# 80	[[80,20],[50,40],[30,10]]	3


def solution(k, dungeons):
    # k : 현재 피로도
    # dungueon : 최소 필요 피로도 / 소모 피로도

    # 모든 던전을 순회하고 싶어.
    # 단, 방문했던 곳은 다시 안갈껀데,
    # 순서가 바뀐다면 갈 수 있어.
    # 즉, a -> b -> c 로 갔다면 다시 b를 가진 않지만,
    # a -> b -> c를 갔다고 해서 a -> c -> b를 안가는건 아니야.
    # visited처리를 할 때, 이미 갔던 곳을 취소하는 동작이 필요할 수 있어.

    visited = [0] * len(dungeons)
    # 현재 피로도 / 현재까지 방문한 곳들의 위치.

    answer = 0

    def dfs(stamina, count):
        nonlocal answer
        answer = max(answer, count)

        # visited처리를 위한 index,
        # 갈 수 있는지 처리를 위한 피로도
        for index, value in enumerate(dungeons):
            min_stamina, need_stamina = value
            # 모든 던전들 가운데,
            #  방문 안한 던전            최소 스테미나를 넘긴 던전
            if visited[index] == 0 and stamina >= min_stamina:
                visited[index] = 1
                dfs(stamina - need_stamina, count + 1)
                visited[index] = 0

    dfs(k, 0)

    return answer


def solution(k, dungeons):
    # k : 현재 피로도
    # dungueon : 최소 필요 피로도 / 소모 피로도

    # 모든 던전을 순회하고 싶어.
    # 단, 방문했던 곳은 다시 안갈껀데,
    # 순서가 바뀐다면 갈 수 있어.
    # 즉, a -> b -> c 로 갔다면 다시 b를 가진 않지만,
    # a -> b -> c를 갔다고 해서 a -> c -> b를 안가는건 아니야.
    # visited처리를 할 때, 이미 갔던 곳을 취소하는 동작이 필요할 수 있어.

    visited = [0] * len(dungeons)
    # 현재 피로도 / 현재까지 방문한 곳들의 위치.

    answer = 0

    def dfs(stamina, lst):
        print(lst)
        # visited처리를 위한 index,
        # 갈 수 있는지 처리를 위한 피로도
        for index, value in enumerate(dungeons):
            min_stamina, need_stamina = value
            # 모든 던전들 가운데,
            #  방문 안한 던전            최소 스테미나를 넘긴 던전
            if visited[index] == 0 and stamina >= min_stamina:
                visited[index] = 1
                lst.append(index)
                dfs(stamina - need_stamina, lst)
                visited[index] = 0
                lst.pop()

    dfs(k, [])

    return answer


solution(800, [[80, 20], [50, 40], [30, 10], [20, 10]])
