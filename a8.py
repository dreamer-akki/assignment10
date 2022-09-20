# 8. Write a python script to print squares of first N natural numbers

n=int(input("Enter the Limit:"))
a=1
for i in range(1,n+1):
    a=i*i
    print(a,end=' ')