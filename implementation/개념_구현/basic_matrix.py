# 기본 2차원 공간 - 행렬(Matrix)
for i in range(5):
    for j in range(5):
        print(f"({i},{j})",end=" ")
    print()

# 방향 벡터 사용
# 동, 북, 서, 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x,y = 2,2

for i in range(4):
    # 다음 위치
    nx = x +dx[i]
    ny = y +dy[i]
    print(nx,ny)