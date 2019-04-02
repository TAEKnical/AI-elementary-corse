b = [1,2,'3']
b=b + [4]
b.append('5')
print(b)
print(type(b))

print('-------------------------------')

c='문'
print(id(c)) ## 메모리 주소
c+='근영'
print(id(c))
#메모리 주소값 바뀜

print('-------------------------------')

d = [1,2,3]
print(id(d))
d.append(5)
print(id(d))
#메모리 주소값 그대로 -> mutable : 내 자신이 변경되었는데 id값은 변하지 않는 자료형.

print('-------------------------------')

d = d+[4]
print(id(d))
# 메모리 주소값 바뀜. +와 append 차이.

print('-------------------------------')

e = (1,2,3)
print(type(e))
print(dir(e))
#튜플도 sequence 타입. sequence는 index와 slice가 가능. 그런데 tuple은 imutable

#기능적 확장성은 list가 좋으나 속도가 떨어짐.
#튜플은 확장성이 없으나 속도가 빠름.
#실제개발에서 속도가 중요할 때는 tuple 사용

print('-------------------------------')

f = [1,2,]
print(f)
g = (1)
print(type(g))
g = (1,)
print(type(g))
g = 1,2,
print(type(g))

print('-------------------------------')

x, y = 1,2
print(x,y)
x=1,2
print(type(x))
#x,y=1,2,3
#print(x,y)

print('-------------------------------')

x,*y=1,2,3
print(x)
print(y)
print(type(x))
print(type(y))
# 컴마로 할당할 때는 개수를 맞춰줘야 한다. 단, 예외적으로 한 개일 때는 튜플로 인식한다.
# *는 나머지를 의미하며, 리스트로 저장한다.

print('-------------------------------')

x,*y,z=1,2,3,4,5,6
print(x, type(x))
print(y, type(y))
print(z, type(z))

print('-------------------------------')

h=[1,2,]
print(dir(h)) # h라는 리스트가 할 수 있는 메소드들을 보여줌

#iterable은 여러 집단에서 하나를 집어낼  수 있는 자료형을 의미. 리스트, 시퀀스 등.
#set도 뽑아낼 수 있는 방법이 있음.
i=[1,2,3,4,5]
i.append([6])
print(i)
i.extend([7])
print(i)
i+=[8]
print(i)

print('-------------------------------')

j = bytearray() #리터럴
print(dir(j))
j.append(67)
print(j)

#바이트와 바이트어레이는 다름.

print('-------------------------------')

k = [1,2,3]
print(k)
print(k.pop())
print(k)

print('-------------------------------')

#set(집합)은 순서가 없고, 중복이 없다. sequence가 아님 -> 인덱스, 슬라이싱 불가.
l = {3,1,2,3,1,2,3,3}
print(l) #{1,2,3}
l = {3,1,2,3,1,2,3,3,}
print(l)
print(dir(l)) #확장이 가능한 메소드들이 있음. set(집합)은 뮤터블.


print('-------------------------------')
#set은 뮤터블이지만, 이뮤터블한 set 이 있음. frozenset.
m = frozenset({1,2,3})
print(m)
print(dir(m))

print('-------------------------------')

o = {'a':1, 'b':2}
print(o['a'])

print('-------------------------------')

p=[1,2,3,4,5]
print(p)
p[1:] = 't'
print(p)

print('-------------------------------')

#a=(1,2,3,4,5)
#a[1]='t' #에러발생. 튜플은 sequence이자 imutable. 바꿀 수 없다.
#print(a)
print('-------------------------------')

#딕셔너리 뷰
#dict.keys(), dict.values(), dict.items()
q = {'a':1, 'b':2, 'c':3}
print(q.keys() , type(q.keys()))
print(q.values(), type(q.values()))
print(q.items(), type(q.items()))
#dictionary는 3가지 관점의 iterable이다.

print('-------------------------------')

#range() -> 시퀀스. iterable.
r = range(10)
print(r)
print(r[5])
print(r[:])
print(r[3:7])
r = range(3,10)
print(r[0])
r = range(3,10,2)
print(r[0],r[1],r[2])

print('-------------------------------')

s = [1,2,3,4,5,6,7,8,9,10]
print(s)
print(s[::2])
print(s[::-1])
print(s[::-2])

print('-------------------------------')


#파이썬 for문에서 in 뒤에는 iterable이 와야 한다.

print('-------------------------------')

print('1' in '1','2','3') # True,2,3 -> 연산자 우선순위 때문
print('1' not in '1','2','3')

print('-------------------------------')

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
#파이썬을 사용하면서 알아야 할 키워드는 33개

#시퀀스 : str, 바이트, 바이트어레이, 리스트, 튜플, 레인지
#시퀀스&뮤터블 : 바이트어레이, 리스트

#pythontutor.com -> 파이썬 코드 작동과정을 시각화해서 보여주는 사이트

print('-------------------------------')
#구구단
for i in range(1,10):
    for j in range(2,10):
        print(j,'x',i,'=',i*j,end='\t')
    print('\n')
#운영체제에 따라 tab키를 space 두 번으로 인식하는 경우가 있기 때문에 space 네번으로 작성하는 습관.


#데이터타입
#숫자형 4가지 : ,float, complex, bool
#숫자형은 imutable.

#문자형 3가지 : str, bytes, bytesarray
#str - UNICODE, 순서 중요
#bytes - 