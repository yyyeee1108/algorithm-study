# 함수 정리

- [함수 정리](#함수-정리)
  - [함수 정의하기](#함수-정의하기)
  - [파라미터 지정하기](#파라미터-지정하기)
  - [global 키워드](#global-키워드)
  - [여러 개의 반환 값](#여러-개의-반환-값)
  - [람다 표현식](#람다-표현식)

함수를 이용하여 불필요한 소스코드의 반복을 줄일 수 있다

### 함수 정의하기

똑같은 코드가 반복적으로 사용될 때 **함수를 정의하여 소스코드의 길이를 줄이자**

기본 형태

```python
def 함수명(매개변수):
    실행할 소스코드
    return 반환 값
```

매개변수와 반환 값은 없어도 된다.

### 파라미터 지정하기

**파라미터의 변수를 직접 지정**할 수 있다

이때, 매개변수의 순서가 달라도 상관X

```python
def add(a,b):
    print('함수의 결과:',a+b)

add(b=3,a=7)
```

여기서 `b=3,a=7`과 같이 지정해주면 함수에서는 a변수에 7, b변수에 3이 오게 된다. 즉, 변수 이름과 같은 것에 대응하는 것임. 그래서 매개변수의 순서가 달라도 상관이 없는 것이다.

### global 키워드

함수 바깥에 선언된 전역 변수를 참조하고 싶을 때, python에서는 global 키워드를 통해 참조해야한다.

다른 언어와 달리 **python에서는 global 키워드 사용 안할 시 참조 안되고 함수 내의 지역변수로 처리하므로 주의하자**

예시)

```python
a = 0 # 전역

def func():
    global a # 전역 a변수 참조, global 키워드 안쓰면 지역변수 취급
    a += 1

for i in range(10):
    func()

print(a)
```

근데 또 전역으로 선언된 리스트의 내부 메소드(예: .append())를 함수 내에서 사용할 때에는 오류 없이 수행된다.

<span style="background-color:tomato">그래도 전역변수 참조시 global 키워드 사용은 꼭 알아두자!! 안헷갈리려면 리스트 변수 또한 global 키워드 사용!
</span>

```python
array = [1,2,3,4,5] #2

def func():
    array = [3,4,5] # 1
    array.append(6)
    print(array) #1 참조

func()
print(array) #2 참조
```

func 내부에서의 print(array) (#1) 에서는 array = [3,4,5] 를 참조,

마지막 줄의 print(array) (#2)에서는 array = [1,2,3,4,5] 를 참조한다

### 여러 개의 반환 값

파이썬에서는 다른 언어와 달리, 여러 개의 반환 값을 가질 수 있다.

예시)

```python
def operator(a,b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    # packing
    return add_var, subtract_var, multiply_var, divide_var

# unpacking
a, b, c, d = operator(7,3)
print(a, b, c, d)
```

여러 개의 반환 값 한 번에 반환 : packing

반환된 값 각각 할당 : unpacking

### 람다 표현식

람다 표현식을 이용하여 함수를 한 줄에 간단하게 작성할 수 있다.

함수 기능이 간단 or 한 번 사용하고 말 때 사용한다.

- 람다 표현식 예시1 - 기본적인 예시

  ```python
  def add(a,b):
      return a+b

  # 일반적인 add() 메서드 사용
  print(add(3,7))

  # 람다 표현식으로 구현한 add() 메서드
  print((lambda a, b: a+b)(3,7))
  ```

  lambda 키워드를 쓴 후 :(콜론) 왼쪽에는 매개변수, 오른쪽에는 반환값을 쓴다.

- 람다 표현식 예시2 - 내장 함수에서 자주 사용되는 람다 함수

  ```python
  # 이 array를 오름차순으로 정리하려 한다
  array = [('홍길동',50),('이순신',32),('아무개',74)]

  # 함수로 사용할 수도 있다.
  def my_key(x):
      return x[1]
  print(sorted(array,key=my_key))

  # 한 번 사용하고 말 것이기에 람다 표현식이 더 간편하다
  print(sorted(array,key=lambda x: x[1]))
  ```

- 람다 표현식 예시3 - 여러 개의 리스트에 적용

  ```python
  # 첫 번째 원소, 두 번째 원소 ... 끼리 더하여 새 리스트로 만들기

  list1 = [1,2,3,4,5]
  list2 = [6,7,8,9,10]

  result = map(lambda a,b : a+b,list1,list2)

  print(list(result))
  ```
