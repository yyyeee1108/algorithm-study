# 내 풀이 - 답안 풀이와 꽤 많이 다름
# 시간복잡도는 아마 O(N)

# 공포도가 x라면 x만큼의 인원으로 구성되는 그룹만 만들고 그 수를 체크하면 된다.

# n = int(input())
# player = list(map(int,input().split()))
# player_s = list(set(player))
# result = 0

# for i in player_s: # set이용 -> 시간복잡도 O(1)
#     result += player.count(i)//i # .count() 시간복잡도 O(N) 

# print(result)


# 답안 예시 풀이
# 오름차순 정렬 뒤 데이터 하나씩 보며 한 번만 순회하여 해결함

n = int(input())
data = list(map(int,input().split()))
data.sort() # 오름차순 정렬

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력