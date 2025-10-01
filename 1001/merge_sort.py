# 시간 복잡도
# O(n)
# O(1)
# O(n**2)

# 기본 정렬.
# min값을 반복적으로 계산해서 정렬.
# 가장 작은 값 : n
# 두번째 작은 값 : n-1
# ... 1 + 2 + ... + n = (1/2)(n)(n+1) -> O(n**2)

# merge sort
# 절반으로 쪼갬. 그 두개가 정렬되어있다고 가정.
# 정렬된 것을 통해 min값을 구하려면 1번의 연산만 있으면 됨
# -> 정렬된 2개 합치기 : n번 연산
# 언제까지 하느냐? 절반으로 쪼갰을 때 1이 남을 때 까지 반복.
# chunk의 사이즈가 1, 2, 4, 8, 16, ... n이 될 때 까지의 횟수 : log(n)
# 시간복잡도 : O(nlog(n))


# 정렬하고 싶은 list가 있음.
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    # 반으로 쪼갬
    mid = len(lst)
    left = lst[:mid]
    right = lst[mid:]

    # 각각 정렬
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # 합침
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
     
    l = 0 # left에서 뽑기,
    r = 0 # right에서 뽑기

    # while l < len(left) and r < len(right):
    while True:
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        # 둘중 하나라도 index에서 벗어나면
        if l == len(left):
            break
        if r == len(right):
            break
    
    result.extend(left[l:])
    result.extend(right[r:])
    return result

# lst = [1, 2, 3]
# lst2 = [3, 4, 5]

# lst.append(lst2)
# print(lst)
# lst.extend(lst2)
# print(lst)