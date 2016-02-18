def hanoi(n,a,b,c):
	if n==1:
		print('move',a ,'to',c)
		return
	else:
		hanoi(n-1,a,c,b)
		print('move',a ,'to',c)
		hanoi(n-1,b,a,c)
hanoi(4,'a','b','c')
