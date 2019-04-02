a = 1
print(type(a))

b=int(1)
print(type(b))

c=bool(-1)
print(c)

d = bytearray()

e = {}
print(type(e)) #dict

f = set()
print(type(f)) #set. 공집합은 리터럴 없이.

g = list() #비어있는 리스트 생성
print(g)
g = list("문근영")
print(g) #한개씩 잘라서.
g = list(range(1))
print(g)
g = [range(10)]
print(g)

h=len({'a':1})#len의 인자는 이터러블
print(h)

#len=3
#print(len('abc'))#파이써는 동적할당을 하기 때문에 키워드를 침범해서 타입에러가 생겨버림.
#del len#할당 해제
#print(len('abc'))


a=1
b=1
print (a is b) #is는 값과 메모리가 모두 같은지 비교한다.

a=1
b=2
print (a is not b)
print("---------------------------------")
print(3 and 1)
print('' and 1) #존재 자체가 거짓은 '',[],(),None 은 진위 비교가 불가능하다.
print([] and 1)
print(() and 1)
print(None and 1)
print(None == False) #==연산은 '값'이 갑은지 파악
print("---------------------------------")

print(3-----4) # --는 +로 취급.
print(2**10) #**는 제곱
print('' in "empty")
print(3*len("three"))

print("---------------------------------")
for i in {'a':1, 'b':3}.items():
	print(i)
print("---------------------------------")

count=0
for i in [1,2,3,1,2,3,1,2,3,]:
	if i==1:
		count+=1
print(count)

print("---------------------------------")

a = dict(a=1,b=2)
print(a)