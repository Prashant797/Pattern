# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# def fact(n):
#     count=1
#     if n==0 or n==1:
#         return 1
    
#     while n>1:
#         count*=n
#         n-=1
#     return count
# print(fact(5))
n=5
for i in range(n):
    for j in range(n):
        if j%2==0:
            if i%2==0:
                print("0",end="")
                print("1",end="")
            else:
                print("1",end="")
                print("0",end="")
    print()

n=3
for i in range(n):
    for j in range(j):
        print("x"*(n-j-i),end="")
    print()