#한숫자가 7개의 빛나는막대로 표시되는 디지털전자시계의 총빛막대카운터로 표현가능한 시간의 수구하기
#

from math import floor

N = 30

def check(num):
    #0->6개,1->2개,2->5개,......9->6숫자
    light = [6,2,5,5,4,5,6,3,7,6]
    return light[floor(num /10)] + light[num % 10]

cnt = 0
for hour in range(0,24):
    for minute in range(0,60):
        for second in range(0,60):
            if(check(hour)+check(minute)+check(second) == N):
                cnt += 1

# lights = [0] * 60
# for i in rang(0, 60):
#    light[i] = check(i)
#메모제이션 ...if(light[hour]+light[minute]+light[second] == N):
print(cnt)