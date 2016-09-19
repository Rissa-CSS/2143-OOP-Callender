"""
Name: Clorissa Callender
Email: ccallender1996@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

print (" Solution A")
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5,1], 4, 2, 6]

print ("Solution B")

lst = [1, 2, 3, 4, 6, 4]
def remove_all(el, lst):  
    lst.remove(el)
    print(lst)
remove_all(6, lst)

print ("Solution C")

def add_this_many(x, y, lst):
    print(lst)
    var = x
    for x in lst:
        if var==x:
            lst.append(y)
          
            
    print(lst)

add_this_many(4, 5, lst)

print ("Solution D")

a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

print ("Solution E")

lst= [1, 2, 3, 4, 5]
def reverse(lst):
	y= len(lst)-1
	for x in lst:
  		lst [y] = x
  		y-=1
	
	print (lst)
  		
reverse(lst)
  		

print ("Solution F")
 
def rotate(lst,k):
    array = lst
    print(array[k-1:] + array[:k-1])
    
rotate(lst,3)

print ("Solution H")

superbowls = {'peyton manning': 1,'joe montana': 4, 'tom brady':3, 'joe flacco': 1}


print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'peyton manning': 1, 'joe montana': 4, ('eli manning', 'giants'): 2, 'tom brady': 3, 'joe flacco': 1}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', 'tom brady': 3, 'peyton manning': 1, ('eli manning', 'giants'): 2, 'joe flacco': 1, 'joe montana': 4}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints:{3: 'cat', 'joe montana': 4, 'tom brady': 3, 'joe flacco': 1, 'peyton manning': 1, ('eli manning', 'giants'): 5}

superbowls [('steelers', '49ers')] = 11
print(superbowls)
#Prints: {3: 'cat', 'tom brady': 3, 'joe montana': 4, 'joe flacco': 1, ('steelers', '49ers'): 11, 'peyton manning': 1, ('eli manning', 'giants'): 5}


print ("Solution I")

print ("Solution J")

d = {1:2, 3:3, 3:2, 4:3}
def rm(d, x):
	
	for key in d.keys():
		if d[key] == x:
			del d[key]
	print (d)		
rm(d,3)
