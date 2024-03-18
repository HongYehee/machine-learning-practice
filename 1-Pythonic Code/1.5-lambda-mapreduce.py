# < Lambda >
# 함수 이름 없이 함수처럼 쓸 수 있는 익명 함수

# general function (함수를 선언해줘야 함)
def f(x, y):
  return x + y

# lambda function (함수 선언 안 해도 실행 가능)
f = lambda x, y: x + y
print(f(1, 4))

f = lambda x: x ** 2
print(f(3))

f = lambda x: x / 2
print(f(3))

# f라고 지정하지 않고도
print((lambda x: x + 1)(5))

# < Map >
# 동일한 함수를 sequence형 자료형(list, tuple)의 각 element에 적용

# python3에서는 map 앞에 list를 붙여줘야 함
ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))

# zip 함수와 같은 효과
ex = [1, 2, 3, 4, 5]
f = lambda x, y: x + y
print(list(map(f, ex, ex)))

# lambda 함수의 filter: 조건을 만족하지 않을 때의 else를 넣어줘야 함
list(map(
  lambda x: x ** 2 if x % 2 == 0 else x,
  ex))
# python3에서는 labmda, map을 안 쓰고 list comprehension으로 하는 게 권장사항이나 ML에서는 많이 사용
[value ** 2 for value in ex]

f = lambda x: x ** 2
print(map(f, ex))
for i in map(f, ex):
  print(i)

# < Reduce >
# map과 달리 list에 똑같은 함수를 적용해서 통합
# map과 같이 많이 씀

# 차례대로 더함
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

# 차례대로 곱함
def factorial(n):
  return reduce(
    lambda x, y: x * y, range(1, n+1))
print(factorial(5))