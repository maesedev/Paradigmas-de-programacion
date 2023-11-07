import math
array = [1,2,3,4,5,6,7,8,9,10] 

print(list(map(lambda x: x*2 ,array)))

tupla = (1,2,3,4,5,6,7,8,9,10)

print(tuple(filter(lambda x: x / math.sqrt(x) > x/2, tupla)))