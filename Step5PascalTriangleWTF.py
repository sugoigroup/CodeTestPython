# 이봐. 파스칼의 삼각형이라는 걸 해보지 않겠나? 무슨 개소리야. 시간이 남니?
#0차수       1
#1차수     1   1
#2차수   1   2  1
#3차수  1  3  3  1
#이런거란다.

N = 45

def count(n):
    coin = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    result = 0
    for c in coin:
        cnt, n = divmod(n, c)
        result += cnt
    return result

row = [0] * (N + 1)
row[0] = 1

for i in range(0, N):
    for j in range(i + 1, 0, -1):
        row[j] += row[j - 1]

total = 0
for i in range(0, N + 1):
    total += count(row[i])

print(total)
