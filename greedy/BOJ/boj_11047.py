n, k = map(int,input().split())

worth = []
for _ in range(n):
    worth.append(int(input()))

result = 0
for i in worth[::-1]:
    result += k//i
    k %= i

print(result)

# 다른 코드 검토
# 기본 코드 원리는 같게 작성함 굿
# 개선 사항
# 1. 중간에 동전 가치 입력받는 부분을 
    # worth = [int(input()) for _ in n]
    # 으로 작성하면 더 간편함
# 2. 역순으로 for문 돌기
    # worth[::-1]
    # reversed(range(worth)) 