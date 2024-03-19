# < Collections >
# list, tuple, dict에 대한 python built-in 확장 자료구조(module)
# deque, OrderedDict, defaultdict, Counter, namedtuple

# 1. deque
# stack과 queue 지원
from collections import deque

deque_list = deque()
for i in range(5):
  deque_list.append(i)
print(deque_list)

deque_list.appendleft(10)
print(deque_list)

# rotate, reverse 등 linked list 특성 지원
deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

print(deque_list)
print(deque(reversed(deque_list)))

deque_list.extend([5, 6, 7])
print(deque_list)

deque_list.extendleft([5, 6, 7])
print(deque_list)

# 2. OrderedDict
# dict와 달리, 데이터 입력 순서대로 dict를 반환 (순서대로 저장)
from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 400

for k, v in d.items():
  print(k, v)

# value 또는 key 값으로 sorting
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
  print(k, v)

for k, v in OrderedDict(sorted(d.items(), key=lambda t:t[1])).items():
  print(k, v)

# 3. defaultdict
# dict type의 값에 기본 값 지정, 신규 값 생성 시 사용
from collections import defaultdict
d = defaultdict(object)
d = defaultdict(lambda: 0)
print(d["first"])

# 단어 수 세기
from collections import OrderedDict

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit!
What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.
However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid.
For example, a while back I received a press release containing the following sentence: "Release 6.0 doubles the level of functionality available, providing organizations of all sizes with a fast-to-deploy, highly robust, and easy-to-use solution to better acquire, retain, and serve customers."
Translation: "The new release does more stuff." Why the extra verbiage? As I explained in the post "Why Marketers Speak Biz Blab", the BS words are simply a way to try to make something unimportant seem important. And, let's face it, a 6.0 release of a product probably isn't all that important.
As a reporter, my immediate response to that press release was that it's not important because it expended an entire sentence saying absolutely nothing. And I assumed (probably rightly) that the company's marketing team was a bunch of idiots.""".lower().split()

# word_count = {}
# for word in text:
#     if word in word_count.keys():
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)

word_count = defaultdict(object)
word_count = defaultdict(lambda: 0)
for word in text:
    word_count[word] += 1
for i, v in OrderedDict(sorted(
        word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(i, v)

# 4. Counter
# sequence type의 data element들의 개수를 dict로 반환
from collections import Counter

c = Counter()
c = Counter('gallahad')
print(c)

# dict type, keyword parameter 등도 처리 가능
c = Counter({'red': 4, 'blue': 2})
print(c)
print(list(c.elements()))

c = Counter(cats=4, dogs=8)
print(c)
print(list(c.elements()))

# 5. namedtuple
# C의 struct 같은 것
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])

x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x=11, y=22))

from collections import namedtuple
import csv
f = open("users.csv", "r")
next(f)
reader = csv.reader(f)
student_list = []
for row in reader:
    student_list.append(row)
    print(row)
print(student_list)

columns = ["user_id", "integration_id", "login_id", "password", "first_name",
            "last_name", "full_name", "sortable_name", "short_name",
            "email", "status"]
Student = namedtuple('Student', columns)
student_namedtupe_list = []
for row in student_list:
    student = Student(*row)
    student_namedtupe_list.append(student)
print(student_namedtupe_list[0])
print(student_namedtupe_list[0].full_name)