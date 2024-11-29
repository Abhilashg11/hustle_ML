## list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if 'a' in i:
        newlist.append(i)

print(newlist)

''' advanced '''

newlist1 = [x for x in fruits ]
print(newlist1)


### readlines 

f = open('text_files/demofile.txt','r')
print(f.readlines(200))
print(f.read(200))
print(f.readline(200))

''' 200 is byte ''' 


#compile or parser and runtime

'''compile'''
# if True
#     print("hello")

'''runtime'''
# print(10/0)

#assignment
x,y,z = 10,20,30
print(x,y,z)

## __str__

class MyClass:
    # pass
    def __str__(self):
        return "this is myclass"

obj = MyClass()
print(obj)


##class decorator

import time

class TimerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} executed in {end_time - start_time} seconds")
        return result

@TimerDecorator
def example_function(n,m):
    total = 0
    for i in range(n):
        total += i
    print(m)
    return total

# Usage
print(example_function(1000000,"time"))