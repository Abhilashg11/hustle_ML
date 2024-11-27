# # # n = int(input("enter the values").strip())
# # li = [1,2,3,4]
# # # for i in range(1, n+1):
# # #     li.append(i)

# # # print(li)
# # text =""
# # for i in li:
# #     text = text+str(i)
# # print(text)



# s = set('HackerRank')
# s.add('H')
# print(s)

# # set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# print(s.add('HackerRank'))

# print( s)
# # set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
l = [[x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1) if(x1+y1+z1)!=n]
    
print(l)

print(dtype(0))