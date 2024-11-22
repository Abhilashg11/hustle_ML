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