from collections import deque
import heapq
def solution(program):
    # a는 프로그램의 점수를 의미하며, 1 ≤ a ≤ 10 을 만족합니다.
    # b는 프로그램이 호출된 시각을 의미하며, 0 ≤ b ≤ 10,000,000을 만족합니다.
    # c는 프로그램의 실행 시간을 의미하며, 1 ≤ c ≤ 1,000을 만족합니다.

    # a, b쌍이 중복되는 프로그램은 입력으로 주어지지 않습니다. 즉, 호출된 시각이 같으면서 점수도 같은 프로그램은 없습니다.
    # 모든 프로그램들이 종료되는 시각과 프로그램의 점수마다 대기시간의 합을 정수 배열에 담아 return 

    # 아직 호출 시간이 안된 애들 : program에 들어있음.
    # 호출 시간이 지나고, 실행 되기 전의 애들 : `어딘가`에 넣어야 함.

    # 이전 실행이 끝났을 때, 
    #     실행이 끝난 시간보다 호출시간이 작은 애들을 program -> `어딘가`에 넣어야 한다.
    #         program을 호출하려면 호출시간 순서대로 정렬되어있는게 편할 것 같음.
    #         program에서 삭제해서 어딘가에 넣어야 하기 때문에 deque를 사용하면 편함. 
    #             그냥 list의 index를 사용해도 괜찮.
    #     `어딘가`에 들어있는 애들 중 우선순위가 가장 높은 애를 실행시킴.
    #         `어딘가`는 우선순위큐가 되어야할 것 같다.

    # program을 호출시간 순으로 정렬하자.
    program.sort(key = lambda x : x[1])
    program = deque(program)
    # 호출 대기를 기다리는 위에서 말한 `어딘가` -> 우선순위큐, 그냥 []를 사용.
    waiting = [] 

    answer = [0]*11

    time = 0 # 지금시간.
    # time = 100 # 실행이 끝난 시간. 예시.
    # time : 실행시키는 시간 으로 정의했는데, 그건 waiting에서 우선순위가 가장 큰 것이 실행되는 것임.
    while waiting or program: # program -> waiting으로 이동, waiting -> 실행. 모든게 실행되어야 일이 끝남.
        # waiting 큐에 뭔가가 들어있어? 그럼 실행시켜.
        # print('waiting', waiting)
        # print('program', program)
        if waiting:
            run = heapq.heappop(waiting) # 우선순위, 호출시간, 지속시간이기 때문에 그냥 heapq써도 이상 없음.
            
            # 문제에서 바라는 대기시간 = 실행시간 - 호출시간
            answer[run[0]] += time - run[1]

            # 실행이 끝나는 시간으로 이동.
            time += run[2]
        else: # 호출된 프로그램이 없느 는 경우, 가장 가까운 program의 시작점으로 이동.
            time = program[0][1]

        while program and program[0][1] <= time:
            p = program.popleft()
            heapq.heappush(waiting, p)

    answer[0] = time
    return answer


solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]	)