# 5. Write a python script to print first N even natural numbers in reverse order.

n=int(input("Enter the Limit: "))
for i in range(n,0,-1):
    if i%2==0:
     print(i,end=' ')