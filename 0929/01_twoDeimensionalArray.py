# 1) 리스트 컴프리헨션
rows, cols = 4, 4
mat = [[i*cols + j for j in range(cols)] for i in range(rows)]
print(mat)


# 2) 범위를 잘라 담기 (chunking)
rows, cols = 4, 4
nums = list(range(rows*cols))
mat = [nums[i:i+cols] for i in range(0, len(nums), cols)]

# 3) 시작값 지정 가능한 함수
def make_grid(rows, cols, start=0):
    return [[start + i*cols + j for j in range(cols)] for i in range(rows)]

mat = make_grid(4, 4)           # 0부터
mat2 = make_grid(3, 5, start=7) # 7부터

# 4) NumPy가 가능하면
# import numpy as np
# rows, cols = 4, 4
# mat = np.arange(rows*cols).reshape(rows, cols).tolist()
