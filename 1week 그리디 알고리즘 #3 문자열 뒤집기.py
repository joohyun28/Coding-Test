s = input()

count1 = 0        #1로 바꾸는 경우의 수
count0 = 0        #0으로 바꾸는 경우의 수

if s[0] == 0:     #만약 첫 번째 수가 0이라면
    count1 += 1   #count1++
    
else:
    count0 += 1   #1이면 count0++

for i in range(len(s) - 1):  #첫 번째 수를 제외한 범위에서
    if s[i] != s[i+1]:       #두 번째 수와 세 번째 수가 다르고
        if s[i+1] =='1':     #세 번째 수가 1이라면
            count0 += 1      #count0++
        else:                #세 번째 수가 0이라면
            count1 += 1      #count1++
            
print(min(count0, count1))   #count의 최솟값 출력
    
