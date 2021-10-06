S = input()

result = int (S[0])

for i in range(1, len(S)): 
    #두 값 중 하나가 1 이하이면 덧셈 
    if int(S[i]) <=1 or result <=1:
        result = result + int(S[i])
    #아니면 곱셈
    else:
        result = result * int(S[i])

print(result)
