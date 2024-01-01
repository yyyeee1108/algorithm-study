# 1 5 2 0 1


# 0 1 이 아니라면 곱이 항상 더 큰 결과

# 좌측에 0이 온다면 더하기로 연산해야함
# 좌측에 1이 온다면 더하기로 

# 우측에 0이 온다면 더하기로 연산해야함
# 우측에 1이 온다면 더하는 것이 더 좋다


# 0이 오면 무조건 더하기029


num = list(map(int,input()))

if num[0] == 0 or num[0] == 1:
    result = num[0]+num[1]
    num = num[2:]
else:
    result = num[0]
    num = num[1:]
    

for i in num:
    
    if i == 0 or i == 1:
        result += i
    else:
        result *= i
    
print(result)
