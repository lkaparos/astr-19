import numpy as np 
import sys

#define the function f(x)
def f(x):
	return x**3+8

#define the main function 
def main ():
	x=9
	result= f(x)
	
#if statement for if the result is > than 27
if f(9)>27:
	print("YAY!")

#print the result of f(9)
	print("f(9)=", f(9))
if __name__=="__main__":
	main()