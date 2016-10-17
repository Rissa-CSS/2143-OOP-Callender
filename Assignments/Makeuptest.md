# Test 1 Makeup - OOP - Fall 2016

-----

## 1: Definitions: 

Using python comments, label all lines that an OOP definition could be applied to.

```python

class Employee:

   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)

emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount

```
-----

#Class
class Employee:
   #Class Variable
   empCount = 0
   
   #Constructor
   def __init__(self, name, salary):
   	  #Data Member 
      self.name = name
      self.salary = salary
      Employee.empCount += 1  
   #Method
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
     
   #Method
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

#Object
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

#Instance
emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount



```python
# place answer here
# use this as a template for your other answers




```

-----

## 2: List Functions

Given the list below:

```python
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
```

**A)** Sort the list

**B)** Add 'Oklahoma' to the list in alphabetical order without sorting the list again. Actually, write a function that would add an item to the list in alphabetical order. Example:

```python States.sort()
def addInOrder(States,Inserts):
	for i in range(len(States)):
		if (States[i] >= Inserts):
			States.insert(i,Inserts)
			break
   	return States
print (addInOrder(States, "Oklahoma"))
```




## 3: Looping over Lists
(10 Points)

Using the following list as an example: `L = [10,20,30,40,50,60,70,80,90,100]` write a function that would divide each value by its index location + 1. Our example list would turn into: `L = [10,10,10,10,10,10,10,10,10,10]`. Remember NOT to get caught up on these values. Your function should work on any list.

Usage:
```python
Answer 3

def addPrevious(L):
	for i in range(len(L)):
		L[i]= L[i]//(i+1)
	return L
print (addPrevious(L))

```

Your answer should consist of just the function definition and none of the usage I provided above.

-----

## 4: Looping over Dictionaries
(10 Points)

Given the following dictionary: 
```python
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" }
```
Iterate over this dictionary, and create a new one that only uses the first three letters of the month. Also make the new months all lowercase. Your new dictionary should look like:

```
abbr_months = {1:"jan",
        2 :"feb",
        3 :"mar",
        4 : "apr", 
     	5 : "may", 
     	6 : "jun", 
    	7 : "jul",
        8 : "aug",
     	9 : "sep", 
    	10 : "oct", 
        11 : "nov",
        12 : "dec" }
```

To help you look up `string slicing` and `lower`. 

Your answer should include just the code that loops and creates the new dictionary.

```python

abbr_months={}
for key in months:
	#print (key,months[key][0:3].lower())
	abbr_months[key]=months[key][0:3].lower()
print (abbr_months)	

```
-----

## 5: Min and Max
(10 Points)

- Assume that pythons built in min , max , and sort functions are broken. Write a function that receives a list then traverses the list and returns the `min` , `max`, and `average` values in a tuple.

```python
def miniStats(L):
	min = L[0]
	max = L[0]
	sumv=0
	for i in range (len(L)):
		sumv += L[i]
		
		if min > L[i]:
			min = L[i]
		if max < L[i]:
			max = L[i]
			
	avg= sumv/len(L)	
	return (min,max,avg)


```

When writing your answer, include the entire function definition (without the comment block).

-----



## 6: Prime Class


Write a class called `myPrimes` that represents a collection of your prime numbers. 
- `addPrime` : 
    - receives a prime number and adds it to your collection of primes
    - it must be checked to make sure it's prime! (should be a private method that does this).
- `removePrime`:
    - a method will remove a prime from your list
- `printPrimes`:
    - this method will print your prime numbers out 
 
```python

class myPrimes (object):
	def __init__ (self,L=[],num=0,prime=False):
		self.L=L
		self.num=num
		self.prime=prime
		
	def addPrime (self,num,prime=False):
		self.num=num
		#self.__checkPrime()
		if self.__checkPrime() == True:
			L.append(num)
		return (L)
		
	def removePrime (self,num):
		self.num=num
		if self.num in L:
			L.remove(num)
		else:
			return "Not in List"
		
	def printPrimes(self):
		#for i in range(len(self.L)):
			return (L)

	def __checkPrime(self):
	
		tempList=[]
		for a in range(self.num):
			if self.num % (a+1) == 0:
				tempList.append(a+1)
		if len(tempList) ==2:
			 self.prime=True
		else:
			 self.prime=False
		return self.prime		

```
-----
