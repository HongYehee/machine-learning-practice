# < Enumerate >

# list에 있는 값들을 추출할 때 index를 붙여줌
for i, v in enumerate(['tic', 'tac', 'toc']):
  print(i, v)

# list에 있는 index와 값을 list로 저장
mylist = ["a", "b", "c", "d"]
print(list(enumerate(mylist)))

# 문장을 list로 만들고, list의 index와 값을 dict로 저장(각 단어가 문장에서 어디에 있는지 위치 찾을 때)
print({i:j for i,j in enumerate('Hanyang University is an academic institute located in South Korea'.split())})


# < Zip >

# 두 개의 list에 있는 값을 병렬로 추출
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
  print(a, b)

# 각 tuple에서 index가 같은 것끼리 묶음
  a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a)
print(b)
print(c)

# 각 tuple에서 index가 같은 것끼리의 합을 list로 (벡터 계산)
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])


# < Enumerate & Zip >
# 두 list에서 같은 index끼리 묶고 index 번호도 붙여줌
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(alist, blist)):
  print(i, a, b)