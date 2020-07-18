# if 문
a = 10
b = 5

if a > b:
    print("a는 b 보다 크다")

# if else 문
print("value 1 input ")
c = input()
print("c value = " + c)

print("value 2 input ")
d = input()

result = ""

if c > d:
    result = "value 1가 더 크다 "
else:
    result = "value 2가 더 크다 "

print("value 1 =" + c + " value2=" + d + " 결과=" + result)
