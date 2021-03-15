# 긴변의 길이가 1000이하에서 만들어질수 있는 정사각형 개수가 딱 20개인 직사각형의 가로세로 길이 쌍이 몇 쌍인지 구하시요? 응?
# 단 직사각형의 가로세로 길ㄹ이를 바꾼 경우는 하나로 취급됨.
# 뭔개소리냐

W, N = 1000, 20

def cut(w, h, n):
    if w==h:
        return n==0
    if w>h:
        w, h = h, w
    q, r = divmod(h, w)
    if (n-q<0) or (r==0):
        return (n-q==0)
    else:
        return cut(w,r,n-q)

cnt = 0
for i in range(1, W+1):
    for j in range(i, W+1):
        if cut(i, j, N):
            cnt += 1

print(cnt)