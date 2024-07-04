n = 10 #배열 크기
data = [0,1,2,3,4,5,6,7,8,9]
# 1번 인덱스부터 7번 인덱스까지 10 늘리기

change = [0 for _ in range(n)]
print(change)
change[1] += 10
change[7+1] -= 10

for i in range(1,n):
    change[i] += change[i-1]

for i in range(n):
    data[i] += change[i]
print(data)
#[0, 11, 12, 13, 14, 15, 16, 7, 8, 9]