# 22.05.14 파이썬 자료형
# 자료형 확인은 type

a = 1
print(type(a))

a = 1.24
print(type(a))

# 나누기는 /
# 몫은 //
a = 2
b = 4
print(a/b)

# 제곱 **
print(a**b)

# string은 큰따옴표 작은따옴표 다 상관없음 막 혼용해서 써도 됨
# \ 백슬래시 쓰면 따옴표를 문자열로 표시해주는거임
print('Python\'s favorite food is perl')
print("hello\nworld")
print("""작은따옴표 큰따옴표 세개 쓰면
엔터도 /n이거 없이 그냥 막 쓸수 있음""")

# 문자열 여러번 출력을 곱하기로 할 수 있음
a = "Python "
b = "is fun"
print(a * 10)

# 문자열 인덱싱
a = "0123456789"
print(a[-2]) #뒤에서 2번째
print(a[0:4]) #0번째부터 4번째 인덱스 미만
print(a[1:4]) #1번째부터 4번째 인덱스 미만
print(a[0:4:2]) #0번째부터 4번째 인덱스 미만인데 2칸 간격씩
print(a[:8]) #비워두면 처음부터 8번째 인덱스 미만
print(a[5:]) #5번째부터 끝까지
print(a[::-2]) #뒤에서부터 2칸 간격씩
print(a[-2::-2]) #86420 출력 문제 풀었음 호정이 알려줬음

# 문자열 포맷팅(+로 안 이어줘도 됨. C언어 처럼 %로 파라미터 매핑)

a = "I eat %d apples." % 3
print(a)

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

# %s로 쓰면 숫자도 그냥 문자열로 바뀌어서 잘 들어감
a = "I ate %d apples. so I was sick for %s days." % (3, day)
print(a)

# 포맷팅을 변수로도 할 수 있음
a = "안녕 {name}, 나이는 {age}".format(age=25, name='승미')
print(a)

# 포맷팅을 문자열 맨 앞에 f 만 입력하면 알아서 다 해줌(python 3.7이상)
name = "int"
a = f"나의 이름은 {name} 입니다"
print(a)

age = 25
name = '승미'
a = f"안녕 {name}, 나이는 {age}"
print(a)


# 정렬과 공백
a = "%f" % 3.42134234
print(a)

a = "%0.4f" % 3.42134234
print(a)

# 문자열 개수 세기
a = "hobbby"
print(a.count('b'))

# 문자열 인덱스 찾기(b가 나오는 가장 첫번째 인덱스)
# 없으면 -1 나옴
a = "hobbby"
print(a.find('b'))
print(a.find('x'))

# join "따옴표" 사이의 문자를 기준으로 삽입해준다
a = ",".join("abcd")
print(a)

a = "#".join(["ab","ab","ab"])
print(a)

# 대문자 / 소문자 / 양쪽공백 제거
a = "hi"
print(a.upper())
a = "HI"
print(a.lower())
a = " H I "
print(a.strip())

# 문자열 바꾸기 / 자르기
a = "life is"
print(a.replace("life", "you"))

a = "life is"
print(a.split())

a = "life:is"
print(a.split(":"))

