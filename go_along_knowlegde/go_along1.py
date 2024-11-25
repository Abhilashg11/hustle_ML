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