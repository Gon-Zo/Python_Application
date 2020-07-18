# 구구단 함수
def multi(val):
    i = 1
    while i <= 9:
        result = val * i
        print(str(val) + " * " + str(i) + " = " + str(result))
        i += 1


multi(2)
