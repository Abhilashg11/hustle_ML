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

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
    
# l = [[x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1) if(x1+y1+z1)!=n]
    
# print(l)

# print(dtype(0))

# def shout(text):
#     return text.upper()
# yell = shout

# def ell(fun):
#     greet = fun("hi how are ")
#     print(greet)

# ell(shout)



# import time

# class TimerDecorator:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         start_time = time.time()
#         result = self.func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function {self.func.__name__} executed in {end_time - start_time} seconds")
#         return result

# @TimerDecorator
# def example_function(n,m):
#     total = 0
#     for i in range(n):
#         total += i
#     print(m)
#     return total

# # Usage
# print(example_function(1000000,"time"))

# class Data:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
        
    
#     def compute(self,a,b,c):
#         r = self.a+self.b+self.c
#         return r


# obj1= Data(2,2,2)
# res = obj1.compute()
# print(res)

# def understand(greet,*args,**kwargs):
#     p = kwargs.get("Punch","!-098789i")
#     end = kwargs.get("elf")
#     for i in args:

#         print(f"{greet} {i} {p}")

#     print(end)

# understand("hello","alice","herald","tiffny",Punch=".",elf="Bye")


# class counter:
#     def __init__(self):
#         self.count = 0
    
#     def __call__(self):
#         self.count += 1
#         print(self.count)

# obj1 = counter()

# obj1()
# # obj1()
# import re
# parts = '2h30m'
# hours = re.search(r'(\d+)h',parts)
# print("hh",hours.group(1))

# hours = sum(int(part.replace('h','')) for part in parts if 'h' in part)
# for part in parts:
#     if 'h' in part:
#         hours = int(part.replace('h', ''))  # Remove 'h' and convert to int
#     elif 'm' in part:
#         print("hi iam in elsif")
#         minutes = int(part.replace('m', ''))  # Remove 'm' and convert to int
    
# #     # Convert hours to minutes and add minutes
# # total_minutes = hours * 60 + minutes
# # print(total_minutes)
# l_m = []
# for _ in range(int(input())):
#     name = input()
#     marks = float(input())
#     l_m.append([name,marks])

# second = sorted(set([marks for name,marks in l_m]))[1]
# s = sorted([name for name,score in l_m if score == second])
# print(s)


#     def fun(val):
#         return val[1] 

# l_m.sort(key = fun)
# print(l_m[-2])

# l = [["lm" ,2],['rh',3],['rt',4]]

# l.sorted()
# print(l)

if __name__=='__main__':
    dic = {}
    n = int(input())
    for _ in range(n):
        name,*marks = input().split()
        dic[name] = marks
    query = input()
    print(dic)
    marks = dic[query]
    marks = list(map(int,marks))
    tot = sum(marks)

print("{:.2f}".format(tot))
print(f"{tot:.2f}")



        
        
        
    