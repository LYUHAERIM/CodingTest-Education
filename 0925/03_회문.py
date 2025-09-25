# 단어를 뒤집었을 때, 자신과 같은 단어가 되면 회문이라고 한다
# 예) 수박이박수, 다시합창합시다

# 회문임을 확인하는 코드를 작성해보시오

# word = str(input())
word = "수박이박수"
trueCnt = 0

for i in range(len(word) // 2):
    if word[i] == word[len(word) - i - 1]:
        trueCnt += 1

if trueCnt == len(word) // 2:
    print("회문이 맞습니다.")
else:
    print("회문이 아닙니다.")
