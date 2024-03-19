# < List Comprehension >

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]

# one dimensional array
result = [a+b for a in case_1 for b in case_2]
print(result)

# two dimensional array
# 바깥 for문(b)이 고정됨
result = [[a+b for a in case_1] for b in case_2]
print(result)