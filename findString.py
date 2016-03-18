#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def countString(file,string,times):
	with open(file) as e:
		count=e.read().count(string)
		if (count!=times):
			return False
		else:
			return True
print(countString('srhba_allow_ip_test.out','1234567890',3))
