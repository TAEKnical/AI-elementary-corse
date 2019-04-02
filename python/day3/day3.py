a={'a':1,'b':2}
print(a)
#a=dict(a=1,a=1) #에러
#print(a)

print("---------------------------------")

def moon(a):
	return a
print(moon(2))

def moon2(a=2):
	return a
print(moon2(3)) #2는 디폴트값일 뿐 , 입력이 들어오면 덮어씌워짐

def moon3(a,b=7):
	return a+b
print(moon3(3))

#def moon4(a=3,b): #에러발생. 
#	return a+b
#print(moon4(,10)) #디폴트 값은 뒤에 있는 파라미터부터 써주어야 함.


print("---------------------------------")

def sun(*,a): # 아스타(*)는 포지셔널(위치에 따른 파라미터 입력) 방식이 아닌 키워드(a=3과 같은) 형식으로만 입력받겠다는 뜻이다.
	return a
print(sun(a=3))

def sun2(b,*,a): #*는 그 뒷부분부터만 적용된다.
	return b,a
print(sun2(1,a=3))

a,*b=1,2,3,4,5
print(a,b)

def sun3(*a): #파라미터를 무한히 입력받음.
	return a
print(sun3(1,2,3,4,5))

a,b,c="문근영"
print(a)

def sun4(**x): # **는 키워드방식으로 입력해야 함.
	return x
print(sun4(x=1))

#def sun4(*a,b):
#	return a
#print(sun4(1,2,3,4,5)) #오류발생

def moon4(**kw):
	if kw=='sun':
		return 1
	return 2
print(moon4(a=1)) # ??

def moon5(**kw):
	if 'sun' in kw.keys():
		print("sun")
	return kw
print(moon5(sun=1))

def star(*x):
	return len(set(x))
print(star(1,2,3,4,2))

#def moon6(a):
#	return a
#print(moon6(5 if a>3 else 7))

print("---------------------------------")

a = lambda : 3 #하나의 함수이자 식. 이름을 안붙이는 익명함수.
#print(a)
print(a())


print("---------------------------------")

a = lambda x,y : x+y
print(a(2,3))


print("---------------------------------")

def moon6(a,b):
	return a+b
print(moon6(1,2))
a=moon6
print(a(1,2)) #함수의 이름을 바꿀 수 있다.
print(moon6(1,2))


print("---------------------------------")

print(list(map(lambda x:x+10, range(100))))


print("---------------------------------")
'''문근영
'''

x = '''
문근영
'''
print(x)

print("---------------------------------")

a=3
b=4
print(a,b)
a,b = b,a
print(a,b)

print("---------------------------------")
def make_incrementor(n):
	return lambda x: x+n

f = make_incrementor(42)
print(f(1))

