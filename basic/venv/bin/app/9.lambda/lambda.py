# lambda 인자 : 표현식

def hap(x, y):
    return x + y

print(hap(10, 20))

value = (lambda x, y: x + y)(10, 20)

print(value)

