# < asterisk(*) >
# 단순 곱셈, 제곱, 가변인자 활용 등 다양하게 사용
# 가변인자: 함수 등애서 여러 개의 값을 한 번에 받을 수 있음

# *args
def asterisk_test(a, *args):
  print(a, args)
  print(type(args))

# 1은 a에 들어가고, 나머지는 tuple 타입으로 args에 들어감
asterisk_test(1, 2, 3, 4, 5, 6)

# **kargs (키워드 인자)
def asterisk_test(a, **kargs):
  print(a, kargs)
  print(type(kargs))

# 1은 a에 들어가고, 나머지는 dic 타입으로 kargs에 들어감
asterisk_test(1, b=2, c=3, d=4, e=5, f=6)

# "unpacking" a container
# sequence형 자료형은 하나의 변수인데(list, tuple 등) 들어있는 값을 나눠서 전달 가능
def asterisk_test(a, *args):
  print(a, args[0]) # tuple이기 때문에 0번째 값으로 명시!
  print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))

# 풀어서 전달하기
def asterisk_test(a, args):
  print(a, *args)
  print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))

# 3개의 element가 있는 1개의 tuple
a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data)

# dict 타입 (**)
def asterisk_test(a, b, c, d):
  print(a, b, c, d)

data = {"b":1, "c":2, "d":3}
asterisk_test(10, **data)

for data in zip(*([1,2], [3,4], [5,6])):
  print(data)
  print(sum(data))