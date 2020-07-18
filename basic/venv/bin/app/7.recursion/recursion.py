# 재귀

def hap(a, b):
    print(a + b)


def gop(a, b):
    print(a * b)


def hap_gop(a, b):
    hap(a, b)
    gop(a, b)


def count_down(num):
    if num == 0:
        print("Stop")
    else:
        print(num)
        count_down(num - 1)


count_down(5)
