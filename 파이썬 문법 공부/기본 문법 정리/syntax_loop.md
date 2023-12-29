# 반복문 정리

- [반복문 정리](#반복문-정리)
  - [for문](#for문)
  - [continue 키워드](#continue-키워드)
  - [break 키워드](#break-키워드)

---

특정한 소스코드를 반복적으로 실행하고자 할 때 사용

while문과 for문이 있는데, python은 코딩테스트에서 for문이 더 간결한 경우가 많음

무한 루프(Infinite Loop) 조심하기

### for문

- 기본형태

  ```python
  for 변수 in 리스트:
      실행할 소스코드
  ```

  'in' 뒤에 오는 **데이터(list, tuple 등)에 포함되어 있는 우너소를 첫 번째 인덱스부터 차례대로 하나씩 방문**

- 차례대로 순회 시

  range(시작 값, 끝 값+1) 사용  
   인자를 하나만 넣으면 자동으로 시작 값은 0이 된다.

### continue 키워드

반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 사용

예시)

```python
result = 0
for i in range(1,10):
    if i%2 == 0:
        continue
    result += i
print(result)
```

### break 키워드

반복문 즉시 탈출 시 사용
