# 가위바위보 에서 N명이 할때, 한번에 승부가 나는경우
N = 100

cnt = 0
# for rock in range(0, N + 1):
#     for scissors in range(0, N - rock + 1):
#         paper = N - rock - scissors
#         all = [rock, scissors, paper]
#         if all.count(max(all)) == 1:
#             cnt += 1
# print(cnt)

# 더 짧게는 OOO|| 처럼 칸만이를 사용하는 방법도 있다

for left in range(0, N + 1):
    for right in range(left, N + 1):
        all = [left, right - left, N - right]
        if all.count(max(all)) == 1:
            cnt += 1
print(cnt)