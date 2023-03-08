Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
bool(1)
True
bopol(-1)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    bopol(-1)
NameError: name 'bopol' is not defined. Did you mean: 'bool'?
bool(-1)
True
bool(0)
False
bool([])
False
bool(['1234'])
True
bool(None)  # python 에서 아무것도 없다는 뜻
False
1 == 2
False
1 == 1
True
1 =1
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1 !=!
SyntaxError: invalid syntax
1 != 2
True
1 != 1
False
1 >= 2
False
1 => 2
SyntaxError: cannot assign to literal
1 <= 2
True
a = 1 <= 2 <=4
b = 1 <= 3 <=4
a == b
True
a !=b
False
type(a)
<class 'bool'>
a
True
a =?
SyntaxError: invalid syntax
print(a)
True
print(a.value)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(a.value)
AttributeError: 'bool' object has no attribute 'value'
a.value()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.value()
AttributeError: 'bool' object has no attribute 'value'
print(a[1])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(a[1])
TypeError: 'bool' object is not subscriptable
c, d, e = a.splt('<=')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c, d, e = a.splt('<=')
AttributeError: 'bool' object has no attribute 'splt'
a = [1, 2, 3, 4, 5, 6]
b = [a, b, c, d, e, f]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b = [a, b, c, d, e, f]
NameError: name 'c' is not defined
b = ['a', 'b', 'c', 'd', 'e', 'f']
c= ['a', 1, 2, 3, ['z', 'b']]
a
[1, 2, 3, 4, 5, 6]
b
['a', 'b', 'c', 'd', 'e', 'f']
c
['a', 1, 2, 3, ['z', 'b']]
a[0]
1
a[-3:]
[4, 5, 6]
>>> a[-3:]   # 뒤에서 부터 3번 인덱스 전까지 출력
[4, 5, 6]
>>> 'a' in b
True
>>> 'z' in c
False
>>> b.index('a')
0
>>> b[b.index(a)]   # b.index('a')는 0번째니까 b[0]이 입력 됨
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b[b.index(a)]   # b.index('a')는 0번째니까 b[0]이 입력 됨
ValueError: [1, 2, 3, 4, 5, 6] is not in list
>>> b[b.index('a')];  # b.index('a')는 0번째니까 b[0]이 입력 됨
'a'
>>> a + b
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f']
>>> a + b + c
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f', 'a', 1, 2, 3, ['z', 'b']]
>>> d = a+ b+ c
>>> d * 2
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f', 'a', 1, 2, 3, ['z', 'b'], 1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f', 'a', 1, 2, 3, ['z', 'b']]
>>> d/a
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d/a
TypeError: unsupported operand type(s) for /: 'list' and 'list'
>>> d -a
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d -a
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> a.append('a')   # 데이터를 영구적으로 추가 가능 맨 뒤로 감
>>>  a
...  
SyntaxError: unexpected indent
>>> a
[1, 2, 3, 4, 5, 6, 'a']
