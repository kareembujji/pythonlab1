Python 3.7.0a2 (v3.7.0a2:f7ac4fe, Oct 17 2017, 17:06:29) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======================== RESTART: Z:/mca/python 1.py ========================
Array after left rotation is:  [3, 4, 5, 6, 7, 1, 2]
>>> def rotateArray(a,d):
	temp=[]
	n=len(a)
	for i in range(0,d):
		temp.append(a[i])
		i = 0
		a=temp.copy()
		return a
	arr = [1,2,3,4,5,6,7]
	print("Array after left rotation is:",end=' ' )
	print(rotate Array(arr,2))
	
SyntaxError: invalid syntax
>>> def rotateArray(a,d):
	temp=[]
	n=len(a)
	for i in range(0,d):
		temp.append(a[i])
		i = 0
		a=temp.copy()
		return a
	arr = [1,2,3,4,5,6,7]
	print("Array after left rotation is:",end=' ' )
	print(rotateArray(arr,2))
	
