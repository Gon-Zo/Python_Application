# 딕셔너리 / dict

# left value = key
# right value = value

a = {
    'title': "not title",
    'content': "not content"
}

print(a)

# key value 로 value 값 출력
print(a['title'])

# title 이라는 key 값 이 있는지 없는지 체크
isTitle = 'title' in a
print(isTitle)
