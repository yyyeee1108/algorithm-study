# 순열/조합을 이용하면 쉽게 풀릴 것 같다

# 첫 시도
# N 입력 받기
# n = int(input())

# 03(3) / 13 / 23 -> 분/초 상관 없이 다 O

# 00 ~ 59 -> 60개 => 60*60 = 3600

# 저 3가지 상황이 아닌 시각에 대해서는
# 분/초로만 따져야 한다
# 3?분 ??초 -> 10*6*10 = 600
# ?3분 ??초 -> 5*

# 315가지

# result = 0
# if n >= 23:
#     result = 3600*3 + 1575*(n-3+1)
# elif n >= 13:
#     result = 3600*2 + 1575*(n-2+1)
# elif n >= 3:
#     result = 3600*1 + 1575*(n-1+1)
# else:
#     result = 1575*(n+1)

# print(result)

# 두 번째 시도
# 완전탐색인 것 알고 다시 풀음
# 하나씩 다 탐색
# 집합으로 풀어보자
# result = 0

# n = int(input())
# for h in range(n+1):
#     for m in range(60):
#         for s in range(60):
#             time_set = set(list(str(h)+str(m)+str(s)))
#             if '3' in time_set:
#                 result += 1
# print(result)


# 답안 예시 -> 완전 탐색(Brute Forcing) 방법 사용
# 'Python은 1초에 2천만번 연산 수행' 이라 생각하면 완전 탐색 방법 사용할 수 있음을 떠올리기 쉬울 것 같다.

# h 입력 받기
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)