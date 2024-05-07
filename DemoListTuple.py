# DemoListTuple.py 
# 주석으로 추가 

lst = [1,2,3]
print( len(lst) )
lst.append(4)
print(lst)
lst.remove(2)
print(lst)

print("---Tuple형식---")
tp = (10, 20, 30)
print(len(tp))

print("---set형식---")
a = {1,2,3,3}
b = {3,4,4,5}
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )

print("---튜플 형식 사용---")
#함수 정의 문법(입력 파라메터 a, b)
def calc(a,b):
    return a+b, a*b 

#호출 
result = calc(3,4)
print(result)

print("id: %s, name: %s" % ("kim", "김유신"))

args = (5,6)
print( calc(*args) )

print("---형식을 변환---")
a = list((10,20,30))
a.append(40)
print(a)

