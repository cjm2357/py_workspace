# 행열로 늘어진 카드 중에서 가장 높은 수의 카드 한장을 뽑는 게임
# 카드가 N * M으로 놓여져 있다.
# N : 행, M : 열
# 행 선택 후 선택한 행에서 가장 낮은 숫자의 카드를 뽑는다.
# 마지막에 선택한 카드에 적힌 숫자 
# 1 <= N , M <= 100

# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

#입력 예시 2
# 2 4
# 7 3 1 8
# 3 3 3 4

n = 3
m = 3
arr = [[3,1,2], [4,1,4], [2,2,2]]
result = 0
for i in range (0, 3) :
    hang = arr[i]
    hang.sort()

for i in range (0, 3) :
    if i==0 or result < arr[i][0] : result = arr[i][0]


print (result)
    