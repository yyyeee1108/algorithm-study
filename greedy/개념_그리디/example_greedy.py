# 당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정합니다. 손님에게 거슬러 주어야 할 돈이 n원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요. 단, 거슬러 줘야 할 돈 n은 항상 10의 배수입니다.

# 시간복잡도 O(K) k는 동전 종류 갯수, 암튼 상수
my_money = (500,100,50,10)

n = int(input("손님 돈: "))

result = 0
for i in my_money:
    result += n//i
    n = n%i
    if n%i == 0: break

print("거스름돈:",result)