Python 3.7.0b4 (v3.7.0b4:eb96c37699, May  2 2018, 19:02:22) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f=open(r'C:\Users\tanvi\Desktop\file operations.csv','r')
>>> r=f.read()
>>> f.close()
>>> r
'color,shape\nBlue,Rectangle \nBlack ,square\nyellow,circle\n'
>>> r=r.split('\n')
>>> keys= r[0].split(',')
>>> keys
['color', 'shape']
>>> d={i:[] for i in keys}
>>> d
{'color': [], 'shape': []}
>>> values=r[1:4]
>>> values
['Blue,Rectangle ', 'Black ,square', 'yellow,circle']
>>> for i,v in enumerate(keys)
SyntaxError: invalid syntax
>>> for i,v in enumerate(keys):
	for val in values:
		d[v]+=[val.split(',')[i]]

		
>>> d
{'color': ['Blue', 'Black ', 'yellow'], 'shape': ['Rectangle ', 'square', 'circle']}
>>> key=d.keys()
>>> key
dict_keys(['color', 'shape'])
>>> key=list(key)
>>> key
['color', 'shape']
>>> value=d.values
>>> value
<built-in method values of dict object at 0x000002A6629A5D80>
>>> value=d.values()
>>> value
dict_values([['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']])
>>> value=str(value)
>>> value
"dict_values([['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']])"
>>> valuevalue=d.values()
>>> value=d.values()
>>> value
dict_values([['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']])
>>> value=list(value)
>>> value
[['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']]
>>> key
['color', 'shape']
>>> value[0]
['Blue', 'Black ', 'yellow']
>>> "".join(value[0])
'BlueBlack yellow'
>>> value[0]
['Blue', 'Black ', 'yellow']
>>> col=value[0]
>>> sha=value[1]
>>> for i,v in col and sha:
	col[i]+=[''.join(sha)[i]]

	
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for i,v in col and sha:
ValueError: too many values to unpack (expected 2)
>>> for i in col:
	for v in sha:
		col[i]+=[''.join(sha)[i]]

		
Traceback (most recent call last):
  File "<pyshell#42>", line 3, in <module>
    col[i]+=[''.join(sha)[i]]
TypeError: list indices must be integers or slices, not str
>>> col=value[0]
>>> col
['Blue', 'Black ', 'yellow']
>>> sha
['Rectangle ', 'square', 'circle']
>>> col[0].join(sha[0])
'RBlueeBluecBluetBlueaBluenBluegBluelBlueeBlue '
>>> col[0] + sha[0]
'BlueRectangle '
>>> col[0] + ','+sha[0]
'Blue,Rectangle '
>>> q=col[0] + ','+sha[0]
>>> w=col[1]+','+sha[1]
>>> e=col[2]+','+sha[2]
>>> q
'Blue,Rectangle '
>>> e
'yellow,circle'
>>> w
'Black ,square'
>>> t=q+w+e
>>> t
'Blue,Rectangle Black ,squareyellow,circle'
>>> t=q+','+w+','+e
>>> t
'Blue,Rectangle ,Black ,square,yellow,circle'
>>> q=str(q)
>>> q
'Blue,Rectangle '
>>> e=str(e)
>>> w=str(w)
>>> t=q+','+w+','+e
>>> 
>>> t
'Blue,Rectangle ,Black ,square,yellow,circle'
>>> w
'Black ,square'
>>> t='q'+','+'w'+','+'e'
>>> t
'q,w,e'
>>> key
['color', 'shape']
>>> key=str(key)
>>> key
"['color', 'shape']"
>>> d
{'color': ['Blue', 'Black ', 'yellow'], 'shape': ['Rectangle ', 'square', 'circle']}
>>> key=d.keys()
>>> key
dict_keys(['color', 'shape'])
>>> key=list(key)
>>> key
['color', 'shape']
>>> t
'q,w,e'
>>> t=q+','+w+','+e
>>> t
'Blue,Rectangle ,Black ,square,yellow,circle'
>>> key[0]+key[1]
'colorshape'
>>> key[0]+','+key[1]
'color,shape'
>>> y=key[0]+','+key[1]
>>> y
'color,shape'
>>> t.join(y)
'cBlue,Rectangle ,Black ,square,yellow,circleoBlue,Rectangle ,Black ,square,yellow,circlelBlue,Rectangle ,Black ,square,yellow,circleoBlue,Rectangle ,Black ,square,yellow,circlerBlue,Rectangle ,Black ,square,yellow,circle,Blue,Rectangle ,Black ,square,yellow,circlesBlue,Rectangle ,Black ,square,yellow,circlehBlue,Rectangle ,Black ,square,yellow,circleaBlue,Rectangle ,Black ,square,yellow,circlepBlue,Rectangle ,Black ,square,yellow,circlee'
>>> t
'Blue,Rectangle ,Black ,square,yellow,circle'
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 

>>> 


>>> 


>>> 

>>> 

>>> 


>>> 
>>> t
'Blue,Rectangle ,Black ,square,yellow,circle'
>>> y
'color,shape'
>>> 
>>> y+t
'color,shapeBlue,Rectangle ,Black ,square,yellow,circle'
>>> p=y+','+t
>>> p
'color,shape,Blue,Rectangle ,Black ,square,yellow,circle'
>>> key[0]+','+key[1]
'color,shape'
>>> q
'Blue,Rectangle '
>>> w
'Black ,square'
>>> e
'yellow,circle'
>>> (key[0]+','+key[1])+(q)+(w)+(e)
'color,shapeBlue,Rectangle Black ,squareyellow,circle'
>>> q=str(q)
>>> q
'Blue,Rectangle '
>>> w=str(w)
>>> e=str(e)
>>> q
'Blue,Rectangle '
>>> w
'Black ,square'
>>> e
'yellow,circle'
>>> w+e
'Black ,squareyellow,circle'
>>> l=list(q,w,e)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    l=list(q,w,e)
TypeError: list expected at most 1 arguments, got 3
>>> l=list(q)
>>> l
['B', 'l', 'u', 'e', ',', 'R', 'e', 'c', 't', 'a', 'n', 'g', 'l', 'e', ' ']
>>> q
'Blue,Rectangle '
>>> l=list(str(q))
>>> l
['B', 'l', 'u', 'e', ',', 'R', 'e', 'c', 't', 'a', 'n', 'g', 'l', 'e', ' ']
>>> q
'Blue,Rectangle '
>>> l= str(list(q))
>>> l
"['B', 'l', 'u', 'e', ',', 'R', 'e', 'c', 't', 'a', 'n', 'g', 'l', 'e', ' ']"
>>> p
'color,shape,Blue,Rectangle ,Black ,square,yellow,circle'
>>> '\n'.join(q)
'B\nl\nu\ne\n,\nR\ne\nc\nt\na\nn\ng\nl\ne\n '
>>> q
'Blue,Rectangle '
>>> d=[]
>>> w
'Black ,square'
>>> e
'yellow,circle'
>>> r
['color,shape', 'Blue,Rectangle ', 'Black ,square', 'yellow,circle', '']
>>> d=[q+w+e]
>>> d
['Blue,Rectangle Black ,squareyellow,circle']
>>> d=[q]
>>> d
['Blue,Rectangle ']
>>> d=[q+','+w+','+e]
>>> d
['Blue,Rectangle ,Black ,square,yellow,circle']
>>> w.append(e)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    w.append(e)
AttributeError: 'str' object has no attribute 'append'
>>> ''.join(q)
'Blue,Rectangle '
>>> ''.join(w)
'Black ,square'
>>> ''.join(e)
'yellow,circle'
>>> a=''.join(q)
>>> b=''.join(w)
>>> c=','.join(e)
>>> a=','.join(q)
>>> b=','.join(w)
>>> k='\n'.join([a+b=c])
SyntaxError: invalid syntax
>>> k='\n'.join([a+b+c])
>>> k
'B,l,u,e,,,R,e,c,t,a,n,g,l,e, B,l,a,c,k, ,,,s,q,u,a,r,ey,e,l,l,o,w,,,c,i,r,c,l,e'
>>> 
=============================== RESTART: Shell ===============================
>>> f=open(r'C:\Users\tanvi\Desktop\file operations.csv','r')
>>> 
==== RESTART: C:/Users/tanvi/AppData/Local/Programs/Python/Python37/sw.py ====
Traceback (most recent call last):
  File "C:/Users/tanvi/AppData/Local/Programs/Python/Python37/sw.py", line 18, in <module>
    key
NameError: name 'key' is not defined
>>> f=open(r'C:\Users\tanvi\Desktop\file operations.csv','r')
>>> r=f.read()
>>> f.close()
>>> r
'color,shape\nBlue,Rectangle \nBlack ,square\nyellow,circle\n'
>>> r=r.split('\n')
>>> d={i:[] for i in keys}
>>> values=r[1:4]
>>> for i,v in enumerate(keys):
	for val in values:
		d[v]+=[val.split(',')[i]]

		
>>> d
{'color': ['Blue', 'Black ', 'yellow'], 'shape': ['Rectangle ', 'square', 'circle']}
>>> key=d.keys
>>> key
<built-in method keys of dict object at 0x0000024C1FBC9630>
>>> key()
dict_keys(['color', 'shape'])
>>> key=','.join(d.keys)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    key=','.join(d.keys)
TypeError: can only join an iterable
>>> key=','.join(d.keys())
>>> key
'color,shape'
>>> d.values()
dict_values([['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']])
>>> d.values()[0]
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    d.values()[0]
TypeError: 'dict_values' object does not support indexing
>>> list(d.values())[0]
['Blue', 'Black ', 'yellow']
>>> list(d.values())[1]
['Rectangle ', 'square', 'circle']
>>> s2=','.join([list(d.values())[0][0],list(d.values())[1][0]])
>>> s2
'Blue,Rectangle '
>>> s3=','.join([list(d.values())[0][1],list(d.values())[1][2]])
>>> s3
'Black ,circle'
>>> s3=','.join([list(d.values())[0][1],list(d.values())[1][1]])
>>> s4=','.join([list(d.values())[0][2],list(d.values())[1][2]])
>>> s3
'Black ,square'
>>> s4
'yellow,circle'
>>> s6='\n'.join([s2,s3,s4])
>>> s6
'Blue,Rectangle \nBlack ,square\nyellow,circle'
>>> s6='\n'.join([key,s2,s3,s4])
>>> s6
'color,shape\nBlue,Rectangle \nBlack ,square\nyellow,circle'
>>> d
{'color': ['Blue', 'Black ', 'yellow'], 'shape': ['Rectangle ', 'square', 'circle']}
>>> p1=[i for i in d.values()]
>>> p1
[['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']]
>>> for i,v enumerate (d.values()):
	
SyntaxError: invalid syntax
>>> for i,v enumerate (d.values):
	
SyntaxError: invalid syntax
>>> d.values()
dict_values([['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']])
>>> [list(d.values())[i][0] for i,_ in enumerate(d.keys())]
['Blue', 'Rectangle ']
>>> [list(d.values())[i][1] for i,_ in enumerate(d.keys())]
['Black ', 'square']
>>> [list(d.values())[i][2] for i,_ in enumerate(d.keys())]
['yellow', 'circle']
>>> ','.join[list(d.values())[i][0] for i,_ in enumerate(d.keys())]
SyntaxError: invalid syntax
>>> ','.join([list(d.values())[i][0] for i,_ in enumerate(d.keys()])
	     
SyntaxError: invalid syntax
>>> 
	     
>>> 
	     
>>> 
	     

>>> 
	     

>>> d
	     
{'color': ['Blue', 'Black ', 'yellow'], 'shape': ['Rectangle ', 'square', 'circle']}
>>> s = ','.join(d.keys())
	     
>>> s
	     
'color,shape'
>>> #s1 = '\n'.join([])
	     
>>> ','.join([list(d.values())[i][0] for i,_ in enumerate(d.keys())])
	     
'Blue,Rectangle '
>>> s1 = '\n'.join([','.join([list(d.values())[i][j] for i,_ in enumerate(d.keys())]) for j in range(len(list(d.values())[0]))])
	     
>>> mystring = '\n'.join([s,s1])
	     
>>> mystring
	     
'color,shape\nBlue,Rectangle \nBlack ,square\nyellow,circle'
>>> d.values()
	     
dict_values([['Blue', 'Black ', 'yellow'], ['Rectangle ', 'square', 'circle']])
>>> 
