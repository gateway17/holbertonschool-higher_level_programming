#!/usr/bin/python3


def add_integer(a, b=98):
	"""Add two numbers, return"""
	if type(a) not in [int, float]:
		raise TypeError('a must be an integer')
	
	elif type(b) not in [int,float]:
		raise TypeError('b must be an integer')
	else:
		int(a, b)
		return (a + b)
