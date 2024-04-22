# N 크기인 배열안에숫자를 M번 조합해서 가장 큰 숫자 만들기
# 같은 Index는 K번만 반복 가능
# K <= M

# [N,M,K]
#  [5,8,3]
arr = [2,4,5,6,4]
m =  8
k = 3

sum = 0
dupli_cnt = 0
index = 0
arr.sort(reverse=True)
while (m > 0) :
    sum += arr[index]
    m -= 1
    if index == 0 :
        dupli_cnt += 1
    else:
        dupli_cnt = 0
        index = 0

    if dupli_cnt == k :
        index +=1

print("sum : " + str(sum))