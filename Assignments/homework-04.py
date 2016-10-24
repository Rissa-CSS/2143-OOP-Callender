"""
Name: Clorissa Callender
Email: ccallender1996@gmail.com
Assignment: Homework 4 - Inheritance
Due: 24 Oct @ 1:00 p.m.
"""


""""
Answer 1 

""""

class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print('...')

class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print('woof!')

class Cat(Pet):
    """"
    Inherits from the Pet class
    """"
	def __init__(self, name, owner, lives=9):
		Pet.__init__(self, name, owner)
		self.lives=lives
	"""
    Sets the language of the animal
    """
	def talk(self):
		print ('Meow')
    
    """
    A cat can only lose a life if they have at least one life. When lives reach zero, the ’is_alive’ variable becomes False.
    
    """
	def lose_life(self):
		if (self.lives>0):
			return (self.lives-1)
		else:
			self.is_alive = False
	
# Creates an instance 
hello = Cat ("Helen", " Mee")

#Calls the lose_life function
print (hello.lose_life())

"""
Answer 2

"""
f = Foo(4)

b = Bar(3)
print(f.a)
# prints what ? 
#4

print(b.a)
# prints what ?
#3

print(f.garply())
# prints what ?
#4

print(b.garply())
# prints what ?
#3

b.a = 9
print(b.garply())
# prints what ?
#9

f.baz = lambda val: val * val
print(f.garply())
# prints what ?
#16