# 코딩 테스트 실전에서 유용한 표준 라이브러리 정리

- [코딩 테스트 실전에서 유용한 표준 라이브러리 정리](#코딩-테스트-실전에서-유용한-표준-라이브러리-정리)
  - [내장함수](#내장함수)
    - [sum()](#sum)
    - [min(), max()](#min-max)
    - [eval()](#eval)
    - [sorted()](#sorted)
  - [itertools](#itertools)
    - [순열 사용시](#순열-사용시)
    - [조합 사용시](#조합-사용시)
  - [heapq](#heapq)
  - [bisect](#bisect)
  - [collections](#collections)
    - [Counter(카운터)](#counter카운터)
  - [math](#math)

## 내장함수

별도의 import 구문 없이도 사용할 수 있는 기본적/필수적 함수

### sum()

```python
result = sum([1,2,3,4,5]) # 합
print(result)
```

### min(), max()

```python
min_result = min(7,3,5,2) # 가장 작은 값 반환 : 2
max_result = max(7,3,5,2) # 가장 큰 값 반환 : 7
print(min_result, max_result)
```

### eval()

```python
result = eval("(3+5)*7") # 사람 입장에서 작성된 수식을 계산하여 수의 형태로 반환
print(result)
```

### sorted()

반복 가능한 객체가 매개변수로 들어왔을 때, 정렬한 결과를 반환한다

- default : 오름차순  
  내림차순 필요시 `sorted(반복객체, reverse=True)`와 같이 사용

  ```python
  # sorted() : 기본은 오름차순 정렬
  result = sorted([9,1,8,5,4])

  # sorted(,reverse=True) : 내림차순 정렬
  reverse_result = sorted([9,1,8,5,4], reverse=True)

  print(result)
  print(reverse_result)
  ```

- key 속성으로 정렬 기준 명시  
  lambda 표현식 함수로 정렬 기준 명시해주는 경우가 많음

  ```python
  # sorted() with key -> 정렬 기준 세워 정렬
  array = [('홍길동',35),('이순신',75),('아무개',50)]

  # 두 번째 인자(x[1])를 기준으로 정렬, 내림차순 정렬
  result = sorted(array,key=lambda x:x[1],reverse=True)

  print(result)
  ```

## itertools

파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공

**순열과 조합** 사용 시 사용  
문제의 경우의 수 짐작 시 값이 천만, 1억 단위를 넘어갈 경우 완전 탐색 시 시간 초과 판정 받을 확률↑

이 때 순열과 조합을 이용하게 되는데, 순열과 조합을 이용하기 위해서는 itertools를 사용한다.

### 순열 사용시

순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열

```python
# itertools에 있는 permutations를 import한다
from itertools import permutations

data = ['A','B','C'] # 데이터 준비

result = list(permutations(data,3)) # 모든 순열 구하기
print(result)
```

실행 결과  
`[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]`

### 조합 사용시

조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것

```python
# itertools에 있는 combinations를 import한다
from itertools import combinations

data = ['A','B','C'] # 데이터 준비

result = list(combinations(data,2)) # 모든 순열 구하기
print(result)
```

실행 결과  
`[('A', 'B'), ('A', 'C'), ('B', 'C')]`

## heapq

힙(Heap) 자료구조 제공

## bisect

이진 탐색(Binary Search) 기능 제공

## collections

덱(deque), 카운터(Counter) 등의 유용한 자료구조 포함

### Counter(카운터)

반복 가능한(iterable) 객체가 주어졌을 때 **내부의 원소 등장 횟수를 세는 기능**

```python
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue']) # 'blue' 등장 횟수 출력
print(counter['green']) # 'green' 등장 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환
```

실행 결과

```
3
1
{'red': 2, 'blue': 3, 'green': 1}
```

## math

필수적인 수학적 기능 제공

- 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수 포함

예시)

```python
# math 라이브러리 import
import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
    # 두 수의 합을 최대 공약수로 나눈 값이 최소 공배수
    return a+b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21,14)) # 최대 공약수(GCD) 계산
print(lcm(21,14)) # 최소 공배수(LCM) 계산
```

실행 결과

```
7
42
```
