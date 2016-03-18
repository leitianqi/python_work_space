# -*- coding:utf-8 -*-

def hanoi(n,a,b,c):
	if n==1:
		print('move',a,'to',c)
		return
	else:
		hanoi(n-1,a,c,b)
		print('move',a,'to',c)
		hanoi(n-1,b,a,c)
		

s=input('please input n:')
n=int(s)
hanoi(n,'a','b','c')
