# reduce ( 함수 , 순서형 자료 )

from functools import reduce

val = reduce(lambda x, y: x + y, range(6))

print(val)
