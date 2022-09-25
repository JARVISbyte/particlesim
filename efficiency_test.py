from vectors import Vector2D as Myvector
import vector 
from time import time as t

N = 1000000
print(f"N = {N}")

x = 1.19
y = 0.63

# testing myvector
print("--- Testing MyVector ---")
a = Myvector(0,0)
start = t()
for i in range(N):
	a += Myvector(x, y)
print(f"Result = ({a.x}, {a.y})")
print(f"Time = {t() - start}\n\n")


# testing vector lib
print("--- Testing vector library ---")
a = vector.obj(x=0,y=0)
start = t()
for i in range(N):
	a += vector.obj(x=x,y=y)
print(f"Result = ({a.x}, {a.y})")
print(f"Time = {t() - start}\n\n")


# results:
"""
--- Testing MyVector ---
Result = (1189999.999969686, 630000.0000040532)
Time = 2.182339906692505


--- Testing vector library ---
Result = (1189999.999969686, 630000.0000040532)
Time = 73.2056245803833
"""
#
#	Vector library is a lot slower
#