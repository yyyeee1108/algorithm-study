# 내 풀이
# import copy

# # L R U D
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# # 현재 위치
# x,y = 1,1 

# # 공간의 크기
# n = int(input())

# # 계획서
# plan = list(input().split())

# for p in plan:
#     cx,cy = copy.deepcopy(x),copy.deepcopy(y) # 현재 위치 저장
    
#     # 이동
#     if p == "L":
#         x += dx[0]
#         y += dy[0]
#     elif p == "R":
#         x += dx[1]
#         y += dy[1]
#     elif p == "U":
#         x += dx[2]
#         y += dy[2]
#     elif p == "D":
#         x += dx[3]
#         y += dy[3]
    
#     # 공간을 벗어나는 움직임 무시
#     # 둘 중 하나가 0 or n+1이면 움직임 무시
#     if x == 0 or x == n+1 or y==0 or y==n+1 :
#         x,y = cx,cy

# print(x,y)

# 답안 예시 풀이

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split() # 자동으로 리스트 형성

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D'] # 이동 방향이 4개 뿐이니 리스트에 담아둔다

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    # nx, ny 라고 설정 뒤 확인 후에 이동 수행하는 방식!!
    # 나는 쓸데없이 원본 위치를 먼저 건드림 -> 최종 이동은 나중으로!
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        # continue 키워드를 통해 다음 반복문으로 바로 넘어가게 한다
        continue
    # 이동 수행
    x, y = nx, ny

print(x,y)
# 쓸데없이 원본 위치 변수를 건드리지 말고 임시 변수(nx, ny)를 통해 이동시켜둔 뒤 예외 조건 확인 후 최종 이동 시키자