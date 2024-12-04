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
# obj1()


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(list(arr[0]))
    
    