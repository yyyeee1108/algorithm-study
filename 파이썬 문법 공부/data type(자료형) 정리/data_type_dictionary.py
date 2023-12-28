# 키(Key)와 값(Value)의 쌍을 데이터로 가진다
# - 리스트와 튜플처럼 순차적 데이터 저장 형식X 키-값에 따른 데이터 저장
# => 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다

# '키(Key)'의 값으로 '변경 불가능한(Immutable) 자료형' 사용 가능

# 파이썬에서는 내부적으로 dictionary 자료형에서 해시 테이블(Hash Table)을 이용
# -> 'O(1)'의 시간복잡도 (데이터의 조회/수정에서)

# 다른 프로그래밍 언어에서는 해시 테이블(Hash Table)로 불림


# 초기화 방법1
data = dict()

# 할당
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

# 초기화 방법2 - 중괄호({})로 묶고 콜론(:)을 통해 초기화 가능
data = {
    '사과' : 'Apple',
    '바나나' : 'Banana',
    '코코넛' : 'Coconut'
}

# 키 값 있는지 확인
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 있습니다.")


# 키와 값을 별도로 뽑아내기 위한 메서드 2가지
# 엄밀히 말하면 dict_keys 라는 객체로 만들어줌
# 완전히 리스트로 사용하고 싶을 때 list로 형변환 필요
    
# 1. keys() : 키 데이터만 뽑아서 리스트로 이용
key_list = data.keys()

# 2. values() : 값 데이터만 뽑아서 리스트로 이용
value_list = data.values()

print("키 리스트:",key_list)
print("값 리스트:",value_list)

# 각 키에 따른 값 하나씩 출력
for key in key_list:
    print(data[key])

# 특정 key에 맵핑되는 값 출력
print(data['바나나'])