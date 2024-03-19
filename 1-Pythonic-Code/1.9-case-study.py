# Case Study: News Categorization

# Q. 비슷한 뉴스를 어떻게 선정할까?
# A. 문자 -> 숫자 -> 벡터

# 컴퓨터는 문자를 그대로 이해하지 못 함
# 문자를 숫자로 바꿔줘야 함
# 숫자로 유사하다는 것은 어떻게 표현할까?
# 유사하다 = (좌표평면상에서) 가깝다
# 어떤 숫자를 좌표평면상에서 표현할 수 있도록 벡터로 바꿔줘야 함

# 문자 -> 벡터
# One-hot Encoding
# Bag of words: 단어별로 index 부여 -> 한 문서의 단어 개수를 vector로 표현

# 유사성: distance measure
# Euclidian distance: 피타고라스 정리, 두 점 사이의 직선 거리
# Cosine similarity: 두 점 사이의 각도

# Data set: 축구와 야구 선수들의 영문 기사 분류해보기

# 파일 불러오기: 폴더명 입력해주면 그 안의 파일들 불러와줌
import os

def get_file_list(dir_name):
  return os.listdir(dir_name)

# 파일별로 내용 읽기
def get_contents(file_list):
  y_class = []
  X_text = []
  class_dict = {1: "0", 2: "0", 3: "0", 4: "0", 5: "1", 6: "1", 7: "1", 8: "1"}

  for file_name in file_list:
    try:
      f = open(file_name, "r", encoding="cp949")
      category = int(file_name.split(os.sep)[1].split("_")[0])
      y_class.append(class_dict[category])
      X_text.append(f.read())
      f.close()
    except UnicodeDecodeError as e:
      print(e)
      print(file_name)
  return X_text, y_class

# 단어사전(corpus) 만들기 + 단어별 index 만들기
def get_cleaned_text(text):
  import re
  text = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@\[\]^_\`{|}~\\\\]', '', text.lower()) # 문장부호 제거
  return text

def get_corpus_dict(text):
  text = [sentence.split() for sentence in text]
  cleaned_words = [get_cleaned_text(word) for words in text for word in words]

  from collections import OrderedDict
  corpus_dict = OrderedDict()
  for i, v in enumerate(set(cleaned_words)):
    corpus_dict[v] = i
  return corpus_dict

# 인덱스별로 Bag of words vector 생성
def get_count_vector(text, corpus):
  text = [sentence.split() for sentence in text]
  word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text]
  X_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))]

  for i, text in enumerate(word_number_list):
    for word_number in text:
      X_vector[i][word_number] += 1
  return X_vector

# 비교하기
import math
def get_cosine_similarity(v1, v2):
  "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
  sumxx, sumxy, sumyy = 0, 0, 0
  for i in range(len(v1)):
      x = v1[i]; y = v2[i]
      sumxx += x*x
      sumyy += y*y
      sumxy += x*y
  return sumxy/math.sqrt(sumxx*sumyy)

# 비교 결과 정리하기
def get_similarity_score(X_vector, source):
  source_vector = X_vector[source]
  similarity_list = []
  for target_vector in X_vector:
      similarity_list.append(
          get_cosine_similarity(source_vector, target_vector))
  return similarity_list

def get_top_n_similarity_news(similarity_score, n):
  import operator
  x = {i:v for i, v in enumerate(similarity_score)}
  sorted_x = sorted(x.items(), key=operator.itemgetter(1))

  return list(reversed(sorted_x))[1:n+1]

# 얼마나 맞는지 측정하기
def get_accuracy(similarity_list, y_class, source_news):
  source_class = y_class[source_news]

  return sum([source_class == y_class[i[0]] for i in similarity_list]) / len(similarity_list)

# main
if __name__ == "__main__":
  dir_name = "news_data"
  file_list = get_file_list(dir_name)
  file_list = [os.path.join(dir_name, file_name) for file_name in file_list]

  X_text, y_class = get_contents(file_list)

  corpus = get_corpus_dict(X_text)
  print("Number of words: {0}".format(len(corpus)))

  X_vector = get_count_vector(X_text, corpus)
  source_number = 10

  result = []

  for i in range(80):
    source_number = i

    similarity_score = get_similarity_score(X_vector, source_number)
    similarity_news = get_top_n_similarity_news(similarity_score, 10)
    accuracy_score = get_accuracy(similarity_news, y_class, source_number)
    result.append(accuracy_score)
  print(sum(result) / 80)