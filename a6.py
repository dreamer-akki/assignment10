# Write a python script to print first N even natural numbers.

n=int(input("Enter the Limit: "))
for i in range(1,n+1):
    if i%2==0:
     print(i,end=' ')