S = input()

result = int (S[0])

for i in range(1, len(S)):
    if int(S[i]) <=1 or result <=1:
        result = result + int(S[i])
    else:
        result = result * int(S[i])

print(result)

